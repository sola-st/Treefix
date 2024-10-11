# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Constructor of ScrollBar.

    Args:
      min_x: (int) left index of the scroll bar on the screen (inclusive).
      min_y: (int) top index of the scroll bar on the screen (inclusive).
      max_x: (int) right index of the scroll bar on the screen (inclusive).
      max_y: (int) bottom index of the scroll bar on the screen (inclusive).
      scroll_position: (int) 0-based location of the screen output. For example,
        if the screen output is scrolled to the top, the value of
        scroll_position should be 0. If it is scrolled to the bottom, the value
        should be output_num_rows - 1.
      output_num_rows: (int) Total number of output rows.

    Raises:
      ValueError: If the width or height of the scroll bar, as determined
       by min_x, max_x, min_y and max_y, is too small.
    """

self._min_x = min_x
self._min_y = min_y
self._max_x = max_x
self._max_y = max_y
self._scroll_position = scroll_position
self._output_num_rows = output_num_rows
self._scroll_bar_height = max_y - min_y + 1

if self._max_x < self._min_x:
    raise ValueError("Insufficient width for ScrollBar (%d)" %
                     (self._max_x - self._min_x + 1))
if self._max_y < self._min_y + 3:
    raise ValueError("Insufficient height for ScrollBar (%d)" %
                     (self._max_y - self._min_y + 1))
