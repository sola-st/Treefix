# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
if os.path.isfile(self._history_file_path):
    try:
        with open(self._history_file_path, "rt") as history_file:
            commands = history_file.readlines()
        self._commands = [command.strip() for command in commands
                          if command.strip()]

        # Limit the size of the history file.
        if len(self._commands) > self._limit:
            self._commands = self._commands[-self._limit:]
            with open(self._history_file_path, "wt") as history_file:
                for command in self._commands:
                    history_file.write(command + "\n")
    except IOError:
        print("WARNING: writing history file failed.")
