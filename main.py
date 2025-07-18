import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv("./api.env")
key=os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=key)

def main():
    print("Hello from agent!")
    if len(sys.argv) == 1:
        print("No user input")
        sys.exit(1)
    user_prompt=sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)
    print(response.text)
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            print(f"User prompt: {user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
