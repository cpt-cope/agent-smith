import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

for _ in range(20):
    
    response = client.models.generate_content(model="gemini-2.5-flash", 
                                            contents=messages,
                                            config=types.GenerateContentConfig(
                                                                                tools=[available_functions], 
                                                                                system_instruction=system_prompt, 
                                                                                ))
                                                                         
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)
        
    if not response.function_calls:
        print(response.text)
        break
    function_results = []
    if response.function_calls:
        for fc in response.function_calls:
            function_call_result = call_function(fc, verbose=args.verbose)
            if  len(function_call_result.parts) == 0:
                raise Exception ("Error: Parts list is empty")
            if function_call_result.parts[0].function_response is None:
                raise Exception ("Error: Function response is None")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception ("Error: Function response is None")
            function_results.append(function_call_result.parts[0])
        messages.append(types.Content(role="user", parts=function_results))
    if api_key is None:
        raise RuntimeError("no API key")

    if response.usage_metadata:
        user_prompt = args.user_prompt
        prompt_count = response.usage_metadata.prompt_token_count
        response_count = response.usage_metadata.candidates_token_count
    else:
        raise RuntimeError("failed API request")

def main():
    if args.verbose:
        print (f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_count}")
        print(f"Response tokens: {response_count}")


    

    if args.verbose:
        print(f"-> {function_call_result.parts[0].function_response.response['result']}")



if __name__ == "__main__":
    main()
