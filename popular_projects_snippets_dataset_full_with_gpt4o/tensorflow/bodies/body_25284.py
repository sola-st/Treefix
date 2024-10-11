# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
try:
    with open(self._history_file_path, "at") as history_file:
        history_file.write(command + "\n")
except IOError:
    pass
