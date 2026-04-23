from google.genai import types
from globals import WORKING_DIR
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file_content import schema_write_file, write_file
from functions.run_python import schema_run_python_file, run_python_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

functions_dict = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_call_part.args["working_directory"] = WORKING_DIR

    function_name = function_call_part.name
    if function_call_part.name in functions_dict:
        function_result = functions_dict[function_name](**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name, response={"result": function_result}
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
