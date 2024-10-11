# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Actually render text output on the screen.

    Wraps the lines according to screen width. Pad lines below according to
    screen height so that the user can scroll the output to a state where
    the last non-empty line is on the top of the screen. Then renders the
    lines on the screen.

    Args:
      output: (RichTextLines) text lines to display on the screen. These lines
        may have widths exceeding the screen width. This method will take care
        of the wrapping.

    Returns:
      (List of int) A list of line indices, in the wrapped output, where there
        are regex matches.
    """

# Wrap the output lines according to screen width.
self._curr_wrapped_output, wrapped_line_indices = (
    debugger_cli_common.wrap_rich_text_lines(output, self._max_x - 2))

# Append lines to curr_wrapped_output so that the user can scroll to a
# state where the last text line is on the top of the output area.
self._curr_wrapped_output.lines.extend([""] * (self._output_num_rows - 1))

# Limit number of lines displayed to avoid curses overflow problems.
if self._curr_wrapped_output.num_lines() > self.max_output_lines:
    self._curr_wrapped_output = self._curr_wrapped_output.slice(
        0, self.max_output_lines)
    self._curr_wrapped_output.lines.append("Output cut off at %d lines!" %
                                           self.max_output_lines)
    self._curr_wrapped_output.font_attr_segs[self.max_output_lines] = [
        (0, len(output.lines[-1]), cli_shared.COLOR_MAGENTA)
    ]

self._display_nav_bar()
self._display_main_menu(self._curr_wrapped_output)

(self._output_pad, self._output_pad_height,
 self._output_pad_width) = self._display_lines(self._curr_wrapped_output,
                                               self._output_num_rows)

# The indices of lines with regex matches (if any) need to be mapped to
# indices of wrapped lines.
exit([
    wrapped_line_indices[line]
    for line in self._unwrapped_regex_match_lines
])
