# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
self._refresh_pad(pad, viewport_top, viewport_left, screen_location_top,
                  screen_location_left, screen_location_bottom,
                  screen_location_right)
self._scroll_bar = ScrollBar(
    self._max_x - 2,
    3,
    self._max_x - 1,
    self._output_num_rows + 1,
    self._output_pad_row,
    self._output_pad_height - self._output_pad_screen_height)

(scroll_pad, _, _) = self._display_lines(
    self._scroll_bar.layout(), self._output_num_rows - 1)
self._refresh_pad(scroll_pad, 0, 0, self._output_top_row + 1,
                  self._max_x - 2, self._output_num_rows + 1,
                  self._max_x - 1)
