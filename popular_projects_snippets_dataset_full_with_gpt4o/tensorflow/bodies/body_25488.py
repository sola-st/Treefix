# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Erase existing text in command textpad."""

existing_len = len(self._command_textbox.gather())
for _ in range(existing_len):
    self._command_textbox.do_command(self.BACKSPACE_KEY)
