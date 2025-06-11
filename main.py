import os, sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types


args = sys.argv[1:] #Takes all the arguments after the script name.

prompt_info = [arg for arg in args if arg != "--verbose"] # Takes all the input except for --verbose

user_prompt = " ".join(prompt_info) #rejoins the strings together.

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
] 

query = client.models.generate_content(model= "gemini-2.0-flash-001", contents=messages) #calls the gemini api using the user_input

if len(sys.argv) > 1: #Checks that input is more than one to confirm that an input has been used otherwise closes the program

    if user_prompt == "": #If not input is entered
        print("No prompt was entered")
        sys.exit(1)
    
    if "--verbose" in sys.argv: #If verbose is used as an argument
        print(f"User prompt: {user_prompt}")
        try:
            print(f"Prompt tokens: {query.usage_metadata.prompt_token_count}")
        except AttributeError as e:
            print(e)
        try:
            print(f"Response tokens: {query.usage_metadata.candidates_token_count}")
        except AttributeError as t:
            print(t)
    
    print(query.text)  #if verbose is not used and prompt is not empty it directly prints the LLM response

    
else:
    print("No arguments were entered.")
    sys.exit(1)






#print(query.usage_metadata)
#print(type(query.usage_metadata))

