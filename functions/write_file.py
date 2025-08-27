import os


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