# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Get the 0-based y coordinate of the scroll block.

    This y coordinate takes into account the presence of the UP and DN buttons
    present at the top and bottom of the ScrollBar. For example, at the home
    location, the return value will be 1; at the bottom location, the return
    value will be self._scroll_bar_height - 2.

    Args:
      screen_coord_sys: (`bool`) whether the return value will be in the
        screen coordinate system.

    Returns:
      (int) 0-based y coordinate of the scroll block, in the ScrollBar
        coordinate system by default. For example,
        when scroll position is at the top, this return value will be 1 (not 0,
        because of the presence of the UP button). When scroll position is at
        the bottom, this return value will be self._scroll_bar_height - 2
        (not self._scroll_bar_height - 1, because of the presence of the DOWN
        button).
    """

rel_block_y = int(
    float(self._scroll_position) / (self._output_num_rows - 1) *
    (self._scroll_bar_height - 3)) + 1
exit(rel_block_y + self._min_y if screen_coord_sys else rel_block_y)
