import os
import signal
import argparse
import subprocess
from .Util import code_executes, gather_files, get_undefined_variables

parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="Python files or .txt file with all file paths", nargs="+")
parser.add_argument(
    "--openai_api_key", help="API Key from OpenAI", default="")

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    for file in files:
        with open(file, "r") as f:
            code = ''.join(f.readlines())

        undefined_variables = get_undefined_variables(code)

        # Original code contains undefined variables
        if undefined_variables:
            from .LLMs.GPT import GPTValuePredictor

            # Predict missing values
            predictor = GPTValuePredictor(args.openai_api_key)
            predictions = predictor.predict(file, undefined_variables)

            imports = predictions['imports']
            imports = imports + '\n\n' if imports else imports
            updated_code = f'{imports}{code}'

            # Code with predicted imports only is not executable
            if not code_executes(updated_code):
                initialization = predictions['initialization']
                initialization = initialization + '\n\n' if initialization else initialization
                updated_code = f'{imports}{initialization}{code}'
        else:
            updated_code = code

        updated_file_path = file.replace('.py', '_updated.py')
        with open(updated_file_path, "w") as f:
            f.write(updated_code)

        # Install missing dependencies
        file_dir_path = os.path.dirname(os.path.realpath(file))
        os.system(f"pipreqs {file_dir_path} --force & pip install -r {file_dir_path}/requirements.txt")

        # Execute file with predicted values
        updated_file_path = file.replace('.py', '_updated.py')
        execution_log_file_path = updated_file_path.replace('.py', '_execution_log.txt')
        execution_log_file = open(execution_log_file_path, "w")

        # run the files (with a timeout)
        try:
            process = subprocess.Popen(
                f"time coverage run --parallel-mode {updated_file_path}", shell=True, start_new_session=True, stdout=execution_log_file, stderr=execution_log_file)
            process.wait(timeout=30)  # seconds
        except subprocess.TimeoutExpired:
            execution_log_file.write("TimeLimit!!!!")
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)

    # Combine coverage data 
    process = subprocess.Popen(
                f"coverage combine", shell=True, start_new_session=True, stdout=execution_log_file, stderr=execution_log_file)

    # Save coverage data
    process = subprocess.Popen(
            f"coverage json", shell=True, start_new_session=True, stdout=execution_log_file, stderr=execution_log_file)

    