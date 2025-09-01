import os
from google.genai import types

def get_file_content(working_directory, file_path):


    mainpath = os.path.join(working_directory, file_path)

    absolute_filepath= os.path.abspath(mainpath)
    absolute_working_directory = os.path.abspath(working_directory)

    

    try:
             
        if not absolute_filepath.startswith(absolute_working_directory):

            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        elif os.path.isfile(mainpath) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        else:
            MAX_CHARS = 10000

            with open(mainpath, "r") as f:
                file_content_string = f.read(MAX_CHARS + 1)
                if len(file_content_string) > MAX_CHARS:
                    file_content_string = file_content_string[:MAX_CHARS]
                    file_content_string += f"[...File {file_path} truncated at 10000 characters]"
                return file_content_string
            
    except Exception as e:
        return f"Error: {str(e)}"
    

schema_get_files_content = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,