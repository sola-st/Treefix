# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with open(self._history_file_path, "wt") as f:
    f.write("help\n")

# Change file to not readable by anyone.
os.chmod(self._history_file_path, 0)

# The creation of a CommandHistory object should not error out.
debugger_cli_common.CommandHistory(
    limit=3, history_file_path=self._history_file_path)

self._restoreFileReadWritePermissions(self._history_file_path)
