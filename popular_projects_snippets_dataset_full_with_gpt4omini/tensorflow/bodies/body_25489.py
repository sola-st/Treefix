# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Render a line of text on the screen.

    Args:
      row: (int) Row index.
      line: (str) The line content.
      attr: curses font attribute.
      color: (str) font foreground color name.

    Raises:
      TypeError: If row is not of type int.
    """

if not isinstance(row, int):
    raise TypeError("Invalid type in row")

if len(line) > self._max_x:
    line = line[:self._max_x]

color_pair = (self._default_color_pair if color is None else
              self._color_pairs[color])

self._addstr(row, 0, line, color_pair | attr)
self._screen_refresh()
