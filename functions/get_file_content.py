import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(name="get_file_content",
                                                    description="Reads a file and returns the contents within a specified character limit within the specified working directory and file and truncates the remainder providing a notification that it was truncated.",
                                                    parameters=types.Schema(type=types.Type.OBJECT,
                                                    properties={"file_path": types.Schema(type=types.Type.STRING,
                                                    description="File to read contents from relative to the working directory",)}))


def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_path = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        if not valid_target_path:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_file_path):
            return (f'Error: File not found or is not a regular file: "{file_path}"')
    

        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
