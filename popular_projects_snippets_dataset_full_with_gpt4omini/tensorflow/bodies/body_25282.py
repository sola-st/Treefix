# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""CommandHistory constructor.

    Args:
      limit: Maximum number of the most recent commands that this instance
        keeps track of, as an int.
      history_file_path: (str) Manually specified path to history file. Used in
        testing.
    """

self._commands = []
self._limit = limit
self._history_file_path = (
    history_file_path or self._get_default_history_file_path())
self._load_history_from_file()
