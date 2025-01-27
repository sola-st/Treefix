# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Display title.

    Args:
      title: (str) The title to display.
      title_color: (str) Color of the title, e.g., "yellow".
    """

# Pad input title str with "-" and space characters to make it pretty.
self._title_line = "--- %s " % title
if len(self._title_line) < self._max_x:
    self._title_line += "-" * (self._max_x - len(self._title_line))

self._screen_draw_text_line(
    self._title_row, self._title_line, color=title_color)
