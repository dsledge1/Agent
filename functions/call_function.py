import os

from google.genai import types
from functions.get_file_content import *
from functions.get_files_info import *
from functions.run_python_file import *
from functions.write_file import *


def call_function(function_call_part, verbose=False):
    function_name=function_call_part.name
    function_args=function_call_part.args
    function_args["working_directory"] = "./calculator"
    if verbose == True:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function {function_name}") #Here?
    function_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file        
    }
    
    func_to_call = ""
    if function_name in function_map:
        func_to_call = function_map[function_name]
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function {function_name}"},
                )
            ]
        )
    results = func_to_call(**function_args) #Or Here?
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": results}
            )
        ]
    )
