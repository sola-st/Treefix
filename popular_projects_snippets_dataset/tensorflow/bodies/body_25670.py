# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
if os.path.isfile(self._history_file_path):
    os.close(self._fd)
    os.remove(self._history_file_path)
