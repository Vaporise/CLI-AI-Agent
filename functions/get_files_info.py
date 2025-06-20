import os


def get_files_info(working_directory, directory=None):
    
    

    if directory == None:
        directory = "."

    mainpath = os.path.join(working_directory, directory)

    absolute_directory = os.path.abspath(mainpath)
    absolute_working_directory = os.path.abspath(working_directory)

    if absolute_directory.startswith(absolute_working_directory):
        pass
    else:
         return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
      
    if os.path.isdir(mainpath) == False:
        return f'Error: "{directory}" is not a directory'

    
    try:
        files_in_directory = os.listdir(mainpath)
    
        all_files = []
        for file in files_in_directory:
        
            current_file_path = os.path.join(mainpath, file)
            current_file_size = os.path.getsize(current_file_path)
            current_file_is_dir = os.path.isdir(current_file_path)
        
            file_info = f"- {file}: file_size={current_file_size} bytes, is_dir={current_file_is_dir}"
            all_files.append(f"{file_info}")
    
        join_files = "\n".join(all_files)
        return join_files
    except Exception as e:
        return f"Error: {str(e)}"



    
    

    
    
    