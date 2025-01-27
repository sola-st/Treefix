# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
if self._nav_bar_pad:
    self._refresh_pad(self._nav_bar_pad, 0, 0, self._nav_bar_row, 0,
                      self._output_pad_screen_location.top, self._max_x)
