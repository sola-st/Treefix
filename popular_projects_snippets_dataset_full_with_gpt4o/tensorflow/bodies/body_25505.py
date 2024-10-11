# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Show array indices for the specified line in the display area.

    Uses the line number to array indices map in the annotations field of the
    RichTextLines object being displayed.
    If the displayed RichTextLines object does not contain such a mapping,
    will do nothing.

    Args:
      line_index: (int) 0-based line index from the top of the display area.
        For example,if line_index == 0, this method will display the array
        indices for the line currently at the top of the display area.

    Returns:
      (list) The array indices at the specified line, if available. None, if
        not available.
    """

# Examine whether the index information is available for the specified line
# number.
pointer = self._output_pad_row + line_index
if (pointer in self._curr_wrapped_output.annotations and
    "i0" in self._curr_wrapped_output.annotations[pointer]):
    indices = self._curr_wrapped_output.annotations[pointer]["i0"]

    array_indices_str = self._format_indices(indices)
    array_indices_info = "@" + array_indices_str

    # TODO(cais): Determine line_index properly given menu pad status.
    #   Test coverage?
    output_top = self._output_top_row
    if self._main_menu_pad:
        output_top += 1

    self._toast(
        array_indices_info,
        color=self._ARRAY_INDICES_COLOR_PAIR,
        line_index=output_top + line_index)

    exit(indices)
else:
    exit(None)
