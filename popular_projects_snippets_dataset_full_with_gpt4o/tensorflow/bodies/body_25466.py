# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Create command window according to screen size."""
if self._command_window:
    del self._command_window

self._command_window = curses.newwin(
    self._command_textbox_height, self._max_x - len(self.CLI_PROMPT),
    self._max_y - self._command_textbox_height, len(self.CLI_PROMPT))
