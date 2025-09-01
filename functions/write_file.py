import os
from google.genai import types

def write_file(working_directory, file_path, content):
    mainpath = os.path.join(working_directory, file_path)

    absolute_filepath= os.path.abspath(mainpath)
    absolute_working_directory = os.path.abspath(working_directory)

    try: 
    
    
        if not absolute_filepath.startswith(absolute_working_directory):

            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
        else: 
            parent_dir = os.path.dirname(absolute_filepath)
            os.makedirs(parent_dir, exist_ok=True)

            with open(absolute_filepath, "w") as f:
                f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ), 
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file_path"
            )
        },
    ),
)
    