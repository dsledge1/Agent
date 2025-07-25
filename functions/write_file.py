import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)              
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
           with open(full_path, "w") as f:
               f.write("")
               print(f'{full_path} did not exist, successfully created it')
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" is not a file'
        with open(full_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites files with specific content at the specific file_path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path of the file to be written or overwritten, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written or overwritten into the file."
            )
        },
    ),
)