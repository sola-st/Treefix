# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Show array indices for the lines at the top and bottom of the output.

    For the top line and bottom line of the output display area, show the
    element indices of the array being displayed.

    Returns:
      If either the top of the bottom row has any matching array indices,
      a dict from line index (0 being the top of the display area, -1
      being the bottom of the display area) to array element indices. For
      example:
        {0: [0, 0], -1: [10, 0]}
      Otherwise, None.
    """

indices_top = self._show_array_index_at_line(0)

output_top = self._output_top_row
if self._main_menu_pad:
    output_top += 1
bottom_line_index = (
    self._output_pad_screen_location.bottom - output_top - 1)
indices_bottom = self._show_array_index_at_line(bottom_line_index)

if indices_top or indices_bottom:
    exit({0: indices_top, -1: indices_bottom})
else:
    exit(None)
