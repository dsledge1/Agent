import os
from config import read_limit

def get_file_content(working_directory, file_path="."):
    try:
        full_path = os.path.join(working_directory, file_path)              
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" is not a file'
        with open(full_path, "r") as f:
            file_content_string = f.read(read_limit)
            if os.path.getsize(full_path) > read_limit:
                file_content_string += f"[]...File {file_path} truncated at 10000 characters]"
            return file_content_string
    except Exception as e:
        return f"Error: {e}"