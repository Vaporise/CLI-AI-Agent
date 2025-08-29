import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    mainpath = os.path.join(working_directory, file_path)

    absolute_filepath= os.path.abspath(mainpath)
    absolute_working_directory = os.path.abspath(working_directory)
    try:

                if not absolute_filepath.startswith(absolute_working_directory):

                        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
                elif os.path.isfile(mainpath) == False:
                        return f'Error: File "{file_path}" not found.'
        
                elif not file_path.endswith('.py'):
                        return f'Error: "{file_path}" is not a Python file.'

                else:
                        completed_process = subprocess.run(['python3',file_path,*args], cwd=working_directory, capture_output = True, timeout = 30)

                        decoded_stdout = completed_process.stdout.decode('utf-8')
                        decoded_stderr = completed_process.stderr.decode('utf-8')

                        final_output = []

                        if decoded_stdout: # If there is the stdout then it's appended to the list
                                final_output.append(f"STDOUT: {decoded_stdout}")

                        if decoded_stderr: # If there is the std error then it's appended to the list.
                                final_output.append(f"STDERR: {decoded_stderr}")
                                

                        if completed_process.returncode and not 0: #If there is an return code then exit with the code.
                            final_output.append(f" Process exited with code {completed_process.returncode}")
                            return "\n".join(final_output)
                        
                        if completed_process.stdout == b'' and completed_process.stderr == b'' and completed_process.returncode == 0:
                            return "No output produced."
 
                        else:
                            return "\n".join(final_output)
                
    except Exception as e:
        return f"Error: executing Python file: {e}"