import argparse
import os
import signal
import subprocess

from l3.Util import gather_files

parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="Python files or .txt file with all file paths", nargs="+")
parser.add_argument(
    "--iids", help="JSON file with instruction IDs", default="iids.json")

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    # run the files (with a timeout)
    for file in files:
        log_file = open(f"{file}_execution_log.txt", "w")
        try:
            process = subprocess.Popen(
                f"time python {file} {args.iids}", shell=True, start_new_session=True, stdout=log_file, stderr=log_file)
            process.wait(timeout=30)  # seconds
        except subprocess.TimeoutExpired:
            log_file.write("TimeLimit!!!!")
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)