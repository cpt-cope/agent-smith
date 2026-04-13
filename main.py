import argparse
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.5-flash", 
                                          contents="user_prompt"
                                         )

if api_key is None:
    raise RuntimeError("no API key")

if response.usage_metadata:
    prompt_count = response.usage_metadata.prompt_token_count
    response_count = response.usage_metadata.candidates_token_count
else:
    raise RuntimeError("failed API request")

def main():
    print("Hello from agent-smith!")
    print(f"Prompt tokens: {prompt_count}")
    print(f"Response tokens: {response_count}")
    print (response.text)


if __name__ == "__main__":
    main()
