import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_path = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        if not valid_target_path:
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_file_path):
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        if target_file_path[-3:] != ".py":
            return (f'Error: "{file_path}" is not a Python file')
        command = ["python", target_file_path]
        if args != None:
            command.extend(args)
        completed_process = subprocess.run(
                                        command, cwd=working_directory_abs, capture_output=True, text=True, timeout=30
                                        )
        return_code = completed_process.returncode
        stdout = completed_process.stdout
        stderr = completed_process.stderr
        message = []
        if return_code != 0:
            message.append(f"Process exited with code {return_code}")
        if not stdout and not stderr:
            message.append(f"No output produced")
        if stdout:
            message.append(f"STDOUT:\n{stdout}")
        if stderr:
            message.append(f"STDERR:\n{stderr}")
        return "\n".join(message)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
