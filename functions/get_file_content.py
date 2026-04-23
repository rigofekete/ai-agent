import os
from globals import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    abs_work_dir = os.path.abspath(working_directory)

    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_work_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if len(file_content_string) == MAX_CHARS:
                # using the wrapped () to allow multi-line expressions if needed when the string is too long
                file_content_string += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )

        return file_content_string

    except Exception as e:
        print(f"Error: {e}")


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read content from the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read the content from, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
