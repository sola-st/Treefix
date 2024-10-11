# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
if self._mouse_enabled != enabled:
    self._mouse_enabled = enabled
    self._screen_set_mousemask()
    self._redraw_output()
