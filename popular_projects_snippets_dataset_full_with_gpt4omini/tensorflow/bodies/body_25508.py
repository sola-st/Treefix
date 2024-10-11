# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Display a one-line message on the screen.

    By default, the toast is displayed in the line right above the scroll bar.
    But the line location can be overridden with the line_index arg.

    Args:
      message: (str) the message to display.
      color: (str) optional color attribute for the message.
      line_index: (int) line index.
    """

pad, _, _ = self._display_lines(
    debugger_cli_common.RichTextLines(
        message,
        font_attr_segs={
            0: [(0, len(message), color or cli_shared.COLOR_WHITE)]}),
    0)

right_end = min(len(message), self._max_x - 2)

if line_index is None:
    line_index = self._output_scroll_row - 1
self._screen_scroll_output_pad(pad, 0, 0, line_index, 0, line_index,
                               right_end)
