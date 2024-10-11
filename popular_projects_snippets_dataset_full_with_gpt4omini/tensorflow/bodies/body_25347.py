# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
output = (0, self._mouse_xy_sequence[self._mouse_counter][0],
          self._mouse_xy_sequence[self._mouse_counter][1], 0,
          curses.BUTTON1_CLICKED)
self._mouse_counter += 1
exit(output)
