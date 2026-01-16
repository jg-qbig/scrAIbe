*** Disclaimer! This README.md was generated using the AI-Agent built in this project (scrAIbe) with the following prompt:
"Write a detailed README.md for this project. The project name is scrAIbe as this is an AI-Agent designed to assist the user to read and write code and text files in an interactive way. The main motivation behind this project was my personal goal to learn how to build an AI-Agent system.

Include these sections in the README.md:

- Title
- Description
- Motivation
- Quick Start
- Usage
- Contributing

If you need the github link for the Quick start section it is https://github.com/jg-qbig/scrAIbe.git. Also include a short disclaimer at the top that the README.md was generated using the AI-Agent built in this project and also include this prompt there. Be true to the project code and look at main.py for the main entrypoint and the files in the functions directory to see the capabilities of the agent. Also remember that this project uses uv to manage python dependencies."
***

# scrAIbe

## Description
scrAIbe is an interactive AI Agent designed to assist users with reading and writing code and text files. Built with the Gemini API, it provides a conversational interface to interact with your codebase, allowing you to list files, read their content, execute Python scripts, and write new files or modify existing ones.

## Motivation
The primary motivation behind developing scrAIbe was my personal goal to learn how to build an AI-Agent system. This project served as a hands-on experience to understand the architecture, design patterns, and implementation challenges involved in creating an intelligent agent that can interact with a file system and execute code based on natural language prompts.

## Quick Start
To get scrAIbe up and running, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jg-qbig/scrAIbe.git
    cd scrAIbe
    ```

2.  **Install dependencies:**
    You can install the project dependencies:
    ```bash
    pip install .
    ```

3.  **Set up your Gemini API Key:**
    Create a `.env` file in the root directory of the project and add your Gemini API key:
    ```
    GEMINI_API_KEY='YOUR_GEMINI_API_KEY'
    ```
    You can obtain a Gemini API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).

## Usage
scrAIbe is a command-line tool. You can interact with it by providing a user prompt as an argument to `main.py`.

```bash
python main.py "Your prompt here"
```

For example:
-   **To list files in the current directory:**
    ```bash
    python main.py "List all files and directories in the current working directory."
    ```
-   **To read the content of a file:**
    ```bash
    python main.py "Read the content of main.py"
    ```
-   **To execute a Python script:**
    ```bash
    python main.py "Run the script my_script.py with arguments 'arg1' and 'arg2'"
    ```
-   **To write content to a file:**
    ```bash
    python main.py "Write 'Hello, World!' to a file named test.txt"
    ```

**Verbose Mode:**
You can enable verbose output to see the agent's thought process, function calls, and token usage by adding the `--verbose` flag:
```bash
python main.py "List all files" --verbose
```

## Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or fix.
3.  Make your changes and ensure tests pass.
4.  Commit your changes with a clear message.
5.  Push your branch to your fork.
6.  Open a pull request to the `main` branch of this repository.
