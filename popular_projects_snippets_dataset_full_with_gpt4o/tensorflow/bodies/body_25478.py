# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
self._max_y, self._max_x = self._stdscr.getmaxyx()
if self._max_x > self._SCREEN_WIDTH_LIMIT:
    self._max_x = self._SCREEN_WIDTH_LIMIT
