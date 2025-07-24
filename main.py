import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import *
from functions.get_file_content import *
from functions.get_files_info import *
from functions.run_python_file import *
from functions.write_file import *
from functions.call_function import *


load_dotenv("./api.env")
key=os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def main():
    print("Hello from agent!")
    if len(sys.argv) == 1:
        print("No user input")
        sys.exit(1)
    user_prompt=sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt)
        )
    verbose = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            print(f"User prompt: {user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}")
            verbose = True

    if response.function_calls:
        for item in response.function_calls:
            function_call_results = call_function(item)
            if not function_call_results.parts[0].function_response.response:
                raise Exception("No Response Found")
            if verbose:
                print(f"-> {function_call_results.parts[0].function_response.response}")

    print(response.text)


if __name__ == "__main__":
    main()
