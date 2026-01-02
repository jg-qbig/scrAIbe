import os
import subprocess

from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run code from the specified file, relative to the current working directory, using the python interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY.STRING,
                description="Any command line arguments that should be provided to the python file at runtime.",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_directory, file_path))

        if os.path.commonpath([working_directory, abs_file_path]) != working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not os.path.basename(abs_file_path).endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]
        if args:
            for a in args:
                command.extend(a)

        output = subprocess.run(
            command, cwd=working_directory, capture_output=True, text=True, timeout=30
        )

        result = []
        if output.returncode != 0:
            result.append(f"Process exited with code {output.returncode}")
        if not output.stdout and not output.stderr:
            result.append("No output produced")
        else:
            result.append(f"STDOUT: {output.stdout}")
            result.append(f"STDERR: {output.stderr}")
        return "\n".join(result)

    except Exception as e:
        print(f"Error: executing Python file: {e}")
