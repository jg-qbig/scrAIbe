import os

from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):
    try:
        working_directory = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(working_directory, directory))

        if (
            os.path.commonpath([working_directory, target_directory])
            != working_directory
        ):
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

        if not os.path.isdir(target_directory):
            return f"Error: '{directory}' is not a directory"

        result = []
        for name in os.listdir(target_directory):
            file_path = os.path.join(target_directory, name)
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            result.append(f"- {name}: file_size={size}, is_dir={is_dir}")
        return "\n".join(result)

    except Exception as e:
        print(f"Error: {e}")
