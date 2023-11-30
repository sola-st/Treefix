import os
import signal
import argparse
import subprocess
from .Util import gather_files

parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="Python files or .txt file with all file paths", nargs="+")

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    #from .LLMs.GPT import GPTValuePredictor

    # run the files (with a timeout)
    for file in files:
        # Predict missing values
        #predictor = GPTValuePredictor()
        #predictor.predict(file)

        # Install missing dependencies
        file_dir_path = os.path.dirname(os.path.realpath(file))
        os.system(f"pipreqs {file_dir_path} --force & pip install -r {file_dir_path}/requirements.txt")

        # Execute file with predicted values
        updated_file_path = file.replace('.py', '_updated.py')
        execution_log_file_path = updated_file_path.replace('.py', '_execution_log.txt')
        execution_log_file = open(execution_log_file_path, "w")

        try:
            process = subprocess.Popen(
                f"time python3 {updated_file_path}", shell=True, start_new_session=True, stdout=execution_log_file, stderr=execution_log_file)
            process.wait(timeout=30)  # seconds
        except subprocess.TimeoutExpired:
            execution_log_file.write("TimeLimit!!!!")
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)

    
