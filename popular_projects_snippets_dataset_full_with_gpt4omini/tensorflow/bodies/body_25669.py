# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._fd, self._history_file_path = tempfile.mkstemp()
self._cmd_hist = debugger_cli_common.CommandHistory(
    limit=3, history_file_path=self._history_file_path)
