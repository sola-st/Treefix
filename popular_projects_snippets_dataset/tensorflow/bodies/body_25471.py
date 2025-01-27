# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
try:
    self._stdscr.addstr(*args)
except curses.error:
    pass
