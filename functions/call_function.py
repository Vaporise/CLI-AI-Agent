from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file
from google.genai import types


def call_function(function_call_part, verbose=False):
    name = function_call_part.name
    args = dict(function_call_part.args)
    
    if verbose:
        print(f"Calling function: {name}({args})")

    else:
        print(f" - Calling function: {name}")

    func_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    func = func_map.get(name)

    if func is None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                name=name,
                response={"error": f"Unknown function: {name}"},
                )
            ],
        )
    

    call_args = {**args, "working_directory": "./calculator"}

    if name == "run_python_file" and "directory" in call_args and "file_path" not in call_args:
        call_args["file_path"] = call_args.pop("directory")

    if name == "get_file_content" and "directory" in call_args and "file_path" not in call_args:
        call_args["file_path"] = call_args.pop("directory")

    if name == "get_files_info" and "path" in call_args and "directory" not in call_args:
        call_args["directory"] = call_args.pop("path")

    if name == "write_file":
        if "path" in call_args and "file_path" not in call_args:
            call_args["file_path"] = call_args.pop("path")

    result = func(**call_args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=name,
                response={"result": result},
            )
        ],
    )

    