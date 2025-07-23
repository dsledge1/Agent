import os
from config import read_limit

def get_file_content(working_directory, file_path):
    try:
                   
        if not os.path.abspath(file_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path):
            return f'Error: "{file_path}" is not a file'
        contents = ""
        with open(file_path, "r") as f:
            file_content_string = f.read(read_limit)
    except Exception as e:
        return f"Error: {e}"