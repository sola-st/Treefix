# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Display text output in a scrollable text pad.

    This method does some preprocessing on the text lines, render them on the
    screen and scroll to the appropriate line. These are done according to regex
    highlighting requests (if any), scroll-to-next-match requests (if any),
    and screen refresh requests (if any).

    TODO(cais): Separate these unrelated request to increase clarity and
      maintainability.

    Args:
      output: A RichTextLines object that is the screen output text.
      is_refresh: (bool) Is this a refreshing display with existing output.
      highlight_regex: (str) Optional string representing the regex used to
        search and highlight in the current screen output.
    """

if not output:
    exit()

if highlight_regex:
    try:
        output = debugger_cli_common.regex_find(
            output, highlight_regex, font_attr=self._SEARCH_HIGHLIGHT_FONT_ATTR)
    except ValueError as e:
        self._error_toast(str(e))
        exit()

    if not is_refresh:
        # Perform new regex search on the current output.
        self._unwrapped_regex_match_lines = output.annotations[
            debugger_cli_common.REGEX_MATCH_LINES_KEY]
    else:
        # Continue scrolling down.
        self._output_pad_row += 1
else:
    self._curr_unwrapped_output = output
    self._unwrapped_regex_match_lines = []

# Display output on the screen.
wrapped_regex_match_lines = self._screen_display_output(output)

# Now that the text lines are displayed on the screen scroll to the
# appropriate line according to previous scrolling state and regex search
# and highlighting state.

if highlight_regex:
    next_match_line = -1
    for match_line in wrapped_regex_match_lines:
        if match_line >= self._output_pad_row:
            next_match_line = match_line
            break

    if next_match_line >= 0:
        self._scroll_output(
            _SCROLL_TO_LINE_INDEX, line_index=next_match_line)
    else:
        # Regex search found no match >= current line number. Display message
        # stating as such.
        self._toast("Pattern not found", color=self._ERROR_TOAST_COLOR_PAIR)
elif is_refresh:
    self._scroll_output(_SCROLL_REFRESH)
elif debugger_cli_common.INIT_SCROLL_POS_KEY in output.annotations:
    line_index = output.annotations[debugger_cli_common.INIT_SCROLL_POS_KEY]
    self._scroll_output(_SCROLL_TO_LINE_INDEX, line_index=line_index)
else:
    self._output_pad_row = 0
    self._scroll_output(_SCROLL_HOME)
