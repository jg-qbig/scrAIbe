import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MAX_ITERATIONS
from prompts import system_prompt
from functions.call_function import available_functions, call_function


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Gemini API key not found.")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    for _ in range(MAX_ITERATIONS):
        response = generate_response(client, messages, args.verbose)
        if response:
            print(f"Final response:\n{response}")
            return

    print(f"Agent exceeded maximum iterations ({MAX_ITERATIONS})")
    sys.exit(1)


def generate_response(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        ),
    )
    if not response.usage_metadata:
        raise RuntimeError("API request failed.")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            if candidate:
                messages.append(candidate.content)

    if not response.function_calls:
        return response.text

    function_results = []
    for call in response.function_calls:
        call_result = call_function(call)
        if (
            not call_result.parts
            or not call_result.parts[0].function_response
            or not call_result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {call.name}")
        if verbose:
            print(f"-> {call_result.parts[0].function_response.response}")
        function_results.append(call_result.parts[0])

    messages.append(types.Content(role="user", parts=function_results))


if __name__ == "__main__":
    main()
