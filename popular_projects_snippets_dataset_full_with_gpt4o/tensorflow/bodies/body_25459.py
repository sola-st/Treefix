# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Get the RichTextLines layout of the scroll bar.

    Returns:
      (debugger_cli_common.RichTextLines) The text layout of the scroll bar.
    """
width = self._max_x - self._min_x + 1
empty_line = " " * width
foreground_font_attr_segs = [(0, width, self.BASE_ATTR)]

if self._output_num_rows > 1:
    block_y = self._block_y()

    if width == 1:
        up_text = "U"
        down_text = "D"
    elif width == 2:
        up_text = "UP"
        down_text = "DN"
    elif width == 3:
        up_text = "UP "
        down_text = "DN "
    else:
        up_text = " UP "
        down_text = "DOWN"

    layout = debugger_cli_common.RichTextLines(
        [up_text], font_attr_segs={0: [(0, width, self.BASE_ATTR)]})
    for i in range(1, self._scroll_bar_height - 1):
        font_attr_segs = foreground_font_attr_segs if i == block_y else None
        layout.append(empty_line, font_attr_segs=font_attr_segs)
    layout.append(down_text, font_attr_segs=foreground_font_attr_segs)
else:
    layout = debugger_cli_common.RichTextLines(
        [empty_line] * self._scroll_bar_height)

exit(layout)
