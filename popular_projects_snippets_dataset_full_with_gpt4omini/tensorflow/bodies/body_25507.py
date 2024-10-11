# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Show candidates (e.g., tab-completion candidates) on multiple lines.

    Args:
      candidates: (list of str) candidates.
    """

if self._curr_unwrapped_output:
    # Force refresh screen output.
    self._scroll_output(_SCROLL_REFRESH)

if not candidates:
    exit()

candidates_prefix = "Candidates: "
candidates_line = candidates_prefix + " ".join(candidates)
candidates_output = debugger_cli_common.RichTextLines(
    candidates_line,
    font_attr_segs={
        0: [(len(candidates_prefix), len(candidates_line), "yellow")]
    })

candidates_output, _ = debugger_cli_common.wrap_rich_text_lines(
    candidates_output, self._max_x - 3)

# Calculate how many lines the candidate text should occupy. Limit it to
# a maximum value.
candidates_num_rows = min(
    len(candidates_output.lines), self._candidates_max_lines)
self._candidates_top_row = (
    self._candidates_bottom_row - candidates_num_rows + 1)

# Render the candidate text on screen.
pad, _, _ = self._display_lines(candidates_output, 0)
self._screen_scroll_output_pad(
    pad, 0, 0, self._candidates_top_row, 0,
    self._candidates_top_row + candidates_num_rows - 1, self._max_x - 2)
