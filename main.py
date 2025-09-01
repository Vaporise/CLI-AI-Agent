import os, sys
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info, available_functions
from functions.call_function import call_function 

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

args = sys.argv[1:] #Takes all the arguments after the script name.

prompt_info = [arg for arg in args if arg != "--verbose"] # Takes all the input except for --verbose

user_prompt = " ".join(prompt_info) #rejoins the strings together.

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
] 

query = client.models.generate_content(
                                       model= "gemini-2.0-flash-001", 
                                       contents=messages,
                                       config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt)
                                       ) #calls the gemini api using the user_input

if len(sys.argv) > 1: #Checks that input is more than one to confirm that an input has been used otherwise closes the program

    if user_prompt == "": #If not input is entered
        print("No prompt was entered")
        sys.exit(1)
    
    if "--verbose" in sys.argv: #If erbose is used as an argument
        print(f"User prompt: {user_prompt}")
        try:
            print(f"Prompt tokens: {query.usage_metadata.prompt_token_count}")
        except AttributeError as e:
            print(e)
        try:
            print(f"Response tokens: {query.usage_metadata.candidates_token_count}")
        except AttributeError as t:
            print(t)

    if not query.function_calls:
        print("Response:")
        print(query.text)  #if verbose is not used and prompt is not empty it directly prints the LLM response

    else:
        for function_call_part in query.function_calls:
            function_call_result = call_function(function_call_part, verbose="--verbose" in sys.argv)

            resp = function_call_result.parts[0].function_response.response
            if resp is None:
                raise RuntimeError("No function response in tool content")

            if "--verbose" in sys.argv:
                print(f"-> {resp}")

    
else:
    print("No arguments were entered.")
    sys.exit(1)






#print(query.usage_metadata)
#print(type(query.usage_metadata))


    