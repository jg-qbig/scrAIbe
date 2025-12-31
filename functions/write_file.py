import os


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
