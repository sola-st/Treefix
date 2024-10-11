# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Display RichTextLines object on screen.

    Args:
      output: A RichTextLines object.
      min_num_rows: (int) Minimum number of output rows.

    Returns:
      1) The text pad object used to display the main text body.
      2) (int) number of rows of the text pad, which may exceed screen size.
      3) (int) number of columns of the text pad.

    Raises:
      ValueError: If input argument "output" is invalid.
    """

if not isinstance(output, debugger_cli_common.RichTextLines):
    raise ValueError(
        "Output is required to be an instance of RichTextLines, but is not.")

self._screen_refresh()

# Number of rows the output area will have.
rows = max(min_num_rows, len(output.lines))

# Size of the output pad, which may exceed screen size and require
# scrolling.
cols = self._max_x - 2

# Create new output pad.
pad = self._screen_new_output_pad(rows, cols)

for i in range(len(output.lines)):
    if i in output.font_attr_segs:
        self._screen_add_line_to_output_pad(
            pad, i, output.lines[i], color_segments=output.font_attr_segs[i])
    else:
        self._screen_add_line_to_output_pad(pad, i, output.lines[i])

exit((pad, rows, cols))
