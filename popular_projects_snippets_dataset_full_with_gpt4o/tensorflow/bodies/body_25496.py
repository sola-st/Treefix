# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Pad the whitespace at the end of a line with the default color pair.

    Prevents spurious color pairs from appearing at the end of the lines in
    certain text terminals.

    Args:
      pad: The curses pad object to operate on.
      row: (`int`) row index.
      line_end_x: (`int`) column index of the end of the line (beginning of
        the whitespace).
    """
if line_end_x < self._max_x - 2:
    pad.addstr(row, line_end_x, " " * (self._max_x - 3 - line_end_x),
               self._default_color_pair)
