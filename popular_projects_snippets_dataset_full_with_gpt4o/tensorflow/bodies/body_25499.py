# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Scroll the output pad.

    Args:
      direction: _SCROLL_REFRESH, _SCROLL_UP, _SCROLL_DOWN, _SCROLL_UP_A_LINE,
        _SCROLL_DOWN_A_LINE, _SCROLL_HOME, _SCROLL_END, _SCROLL_TO_LINE_INDEX
      line_index: (int) Specifies the zero-based line index to scroll to.
        Applicable only if direction is _SCROLL_TO_LINE_INDEX.

    Raises:
      ValueError: On invalid scroll direction.
      TypeError: If line_index is not int and direction is
        _SCROLL_TO_LINE_INDEX.
    """

if not self._output_pad:
    # No output pad is present. Do nothing.
    exit()

if direction == _SCROLL_REFRESH:
    pass
elif direction == _SCROLL_UP:
    # Scroll up.
    self._output_pad_row -= int(self._output_num_rows / 3)
    if self._output_pad_row < 0:
        self._output_pad_row = 0
elif direction == _SCROLL_DOWN:
    # Scroll down.
    self._output_pad_row += int(self._output_num_rows / 3)
    if (self._output_pad_row >
        self._output_pad_height - self._output_pad_screen_height - 1):
        self._output_pad_row = (
            self._output_pad_height - self._output_pad_screen_height - 1)
elif direction == _SCROLL_UP_A_LINE:
    # Scroll up a line
    if self._output_pad_row - 1 >= 0:
        self._output_pad_row -= 1
elif direction == _SCROLL_DOWN_A_LINE:
    # Scroll down a line
    if self._output_pad_row + 1 < (
        self._output_pad_height - self._output_pad_screen_height):
        self._output_pad_row += 1
elif direction == _SCROLL_HOME:
    # Scroll to top
    self._output_pad_row = 0
elif direction == _SCROLL_END:
    # Scroll to bottom
    self._output_pad_row = (
        self._output_pad_height - self._output_pad_screen_height - 1)
elif direction == _SCROLL_TO_LINE_INDEX:
    if not isinstance(line_index, int):
        raise TypeError("Invalid line_index type (%s) under mode %s" %
                        (type(line_index), _SCROLL_TO_LINE_INDEX))
    self._output_pad_row = line_index
else:
    raise ValueError("Unsupported scroll mode: %s" % direction)

self._nav_history.update_scroll_position(self._output_pad_row)

# Actually scroll the output pad: refresh with new location.
output_pad_top = self._output_pad_screen_location.top
if self._main_menu_pad:
    output_pad_top += 1
self._screen_scroll_output_pad(self._output_pad, self._output_pad_row, 0,
                               output_pad_top,
                               self._output_pad_screen_location.left,
                               self._output_pad_screen_location.bottom,
                               self._output_pad_screen_location.right)
self._screen_render_nav_bar()
self._screen_render_menu_pad()

self._scroll_info = self._compile_ui_status_summary()
self._screen_draw_text_line(
    self._output_scroll_row,
    self._scroll_info,
    color=self._STATUS_BAR_COLOR_PAIR)
