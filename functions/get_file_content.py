import os

from google.genai import types

from config import MAX_CHARS


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns content of the specified file, relative to the current working directory, as a string up to a maximum of {MAX_CHARS} characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to return content from, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(working_directory, file_path))

        if os.path.commonpath([working_directory, file_path]) != working_directory:
            return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"

        if not os.path.isfile(file_path):
            return f"Error: File not found or is not a regular file: '{file_path}'"

        with open(file_path, "r", encoding="utf8") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (
                    f"[...File '{file_path}' truncated at {MAX_CHARS} characters]"
                )
        return file_content

    except Exception as e:
        print(f"Error: {e}")
