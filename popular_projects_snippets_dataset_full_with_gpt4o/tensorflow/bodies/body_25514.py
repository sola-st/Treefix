# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
if self._mouse_enabled:
    curses.mousemask(curses.BUTTON1_RELEASED | curses.BUTTON1_PRESSED)
else:
    curses.mousemask(0)
