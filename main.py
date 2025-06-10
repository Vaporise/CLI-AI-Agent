import os, sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]



if len(sys.argv) > 1:
    query = client.models.generate_content(model= "gemini-2.0-flash-001", contents=messages)
    print(query.text)

    try:
        print(f"Prompt tokens: {query.usage_metadata.prompt_token_count}")
    except AttributeError as e:
        print(e)
    try:
        print(f"Response tokens: {query.usage_metadata.candidates_token_count}")
    except AttributeError as t:
        print(t)
else:
    print("No arguments were entered.")
    sys.exit(1)






#print(query.usage_metadata)
#print(type(query.usage_metadata))

