import os

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