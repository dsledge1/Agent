import os
from config import read_limit
from google.genai import types

def get_file_content(working_directory, file_path="."):
    try:
        full_path = os.path.join(working_directory, file_path)              
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" is not a file'
        with open(full_path, "r") as f:
            file_content_string = f.read(read_limit)
            if os.path.getsize(full_path) > read_limit:
                file_content_string += f"[]...File {file_path} truncated at 10000 characters]"
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of the specified file at file_path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to read from, relative to the working directory.",
            ),
        },
    ),
)