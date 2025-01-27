# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui.py
readline.parse_and_bind("set editing-mode emacs")

# Disable default readline delimiter in order to receive the full text
# (not just the last word) in the completer.
readline.set_completer_delims("\n")
readline.set_completer(self._readline_complete)
readline.parse_and_bind("tab: complete")

self._input = input
