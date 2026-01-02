import os

from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the specified content to the specified file, relative to the current working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write content to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the specified file.",
            ),
        },
        required=["file_path", "content"],
    ),
)


def write_file(working_directory, file_path, content):
    try:
        working_directory = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(working_directory, file_path))

        if os.path.commonpath([working_directory, file_path]) != working_directory:
            return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"

        if os.path.isdir(file_path):
            return f"Error: Cannot write to '{file_path}' as it is a directory"

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf8") as f:
            f.write(content)

        return (
            f"Successfully wrote to '{file_path}' ({len(content)} characters written)"
        )

    except Exception as e:
        print(f"Error: {e}")
