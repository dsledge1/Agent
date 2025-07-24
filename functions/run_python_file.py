import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)              
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found'
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" is not a file'
        if not full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        result = subprocess.run(["python3", file_path] + args, timeout=30, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_directory, text=True)
        if result.returncode != 0:
            return f'STDOUT:{result.stdout}\nSTDERR:{result.stderr}\nProcess exited with code {result.returncode}'
        if not result.stdout and not result.stderr:
            return "No output produced." 
        return f'STDOUT:{result.stdout}\nSTDERR:{result.stderr}'

    except Exception as e:
        return f"Error: executing Pything file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes Python file at file_path with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path of the .py file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional, arguments to include in the file being run.",
            )
        },
    ),
)