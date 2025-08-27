import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    mainpath = os.path.join(working_directory, file_path)

    absolute_filepath= os.path.abspath(mainpath)
    absolute_working_directory = os.path.abspath(working_directory)

    if not absolute_filepath.startswith(absolute_working_directory):

            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    elif os.path.isfile(mainpath) == False:
            return f'Error: File "{file_path}" not found.'
    
    elif not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

    else:
           program_run = subprocess.run(args, capture_output = True, timeout = 30,)