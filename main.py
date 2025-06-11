import os, sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types


args = sys.argv[1:]

prompt_info = [arg for arg in args if arg != "--verbose"]

user_prompt = " ".join(prompt_info)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

query = client.models.generate_content(model= "gemini-2.0-flash-001", contents=messages)

if len(sys.argv) > 1:
    
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        try:
            print(f"Prompt tokens: {query.usage_metadata.prompt_token_count}")
        except AttributeError as e:
            print(e)
        try:
            print(f"Response tokens: {query.usage_metadata.candidates_token_count}")
        except AttributeError as t:
            print(t)
    
    print(query.text)  

    
else:
    print("No arguments were entered.")
    sys.exit(1)






#print(query.usage_metadata)
#print(type(query.usage_metadata))

