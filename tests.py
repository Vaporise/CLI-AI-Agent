from functions.get_files_info import get_files_content

get_file_content("calculator", "main.py")
get_file_content("calculator", "pkg/calculator.py")
get_file_content("calculator", "/bin/cat") (this should return an error string)