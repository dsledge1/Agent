import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv("./api.env")
key=os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=key)

def main():
    print("Hello from agent!")
    query=sys.argv[0]
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=query)
    if contents == None:
        print("No user input")
        sys.exit(1)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
