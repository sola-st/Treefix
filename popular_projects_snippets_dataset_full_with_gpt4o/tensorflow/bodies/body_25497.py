# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Render a line in a text pad.

    Assumes: segments in color_segments are sorted in ascending order of the
    beginning index.
    Note: Gaps between the segments are allowed and will be fixed in with a
    default color.

    Args:
      pad: The text pad to render the line in.
      row: Row index, as an int.
      txt: The text to be displayed on the specified row, as a str.
      color_segments: A list of 3-tuples. Each tuple represents the beginning
        and the end of a color segment, in the form of a right-open interval:
        [start, end). The last element of the tuple is a color string, e.g.,
        "red".

    Raisee:
      TypeError: If color_segments is not of type list.
    """

if not color_segments:
    pad.addstr(row, 0, txt, self._default_color_pair)
    self._pad_line_end_with_whitespace(pad, row, len(txt))
    exit()

if not isinstance(color_segments, list):
    raise TypeError("Input color_segments needs to be a list, but is not.")

all_segments = []
all_color_pairs = []

# Process the beginning.
if color_segments[0][0] == 0:
    pass
else:
    all_segments.append((0, color_segments[0][0]))
    all_color_pairs.append(self._default_color_pair)

for (curr_start, curr_end, curr_attrs), (next_start, _, _) in zip(
    color_segments, color_segments[1:] + [(len(txt), None, None)]):
    all_segments.append((curr_start, curr_end))

    if not isinstance(curr_attrs, list):
        curr_attrs = [curr_attrs]

    curses_attr = curses.A_NORMAL
    for attr in curr_attrs:
        if (self._mouse_enabled and
            isinstance(attr, debugger_cli_common.MenuItem)):
            curses_attr |= curses.A_UNDERLINE
        else:
            curses_attr |= self._color_pairs.get(attr, self._default_color_pair)
    all_color_pairs.append(curses_attr)

    if curr_end < next_start:
        # Fill in the gap with the default color.
        all_segments.append((curr_end, next_start))
        all_color_pairs.append(self._default_color_pair)

    # Finally, draw all the segments.
for segment, color_pair in zip(all_segments, all_color_pairs):
    if segment[1] < self._max_x:
        pad.addstr(row, segment[0], txt[segment[0]:segment[1]], color_pair)
if all_segments:
    self._pad_line_end_with_whitespace(pad, row, all_segments[-1][1])
