# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
if self._output_num_rows <= 1:
    exit(None)
elif mouse_y == self._min_y:
    exit(_SCROLL_UP_A_LINE)
elif mouse_y == self._max_y:
    exit(_SCROLL_DOWN_A_LINE)
elif (mouse_y > self._block_y(screen_coord_sys=True) and
      mouse_y < self._max_y):
    exit(_SCROLL_DOWN)
elif (mouse_y < self._block_y(screen_coord_sys=True) and
      mouse_y > self._min_y):
    exit(_SCROLL_UP)
else:
    exit(None)
