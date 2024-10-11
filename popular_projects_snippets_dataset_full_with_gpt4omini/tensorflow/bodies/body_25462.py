# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Initialize the layout of UI components.

    Initialize the location and size of UI components such as command textbox
    and output region according to the terminal size.
    """

# NamedTuple for rectangular locations on screen
self.rectangle = collections.namedtuple("rectangle",
                                        "top left bottom right")

# Height of command text box
self._command_textbox_height = 2

self._title_row = 0

# Row index of the Navigation Bar (i.e., the bar that contains forward and
# backward buttons and displays the current command line).
self._nav_bar_row = 1

# Top row index of the output pad.
# A "pad" is a curses object that holds lines of text and not limited to
# screen size. It can be rendered on the screen partially with scroll
# parameters specified.
self._output_top_row = 2

# Number of rows that the output pad has.
self._output_num_rows = (
    self._max_y - self._output_top_row - self._command_textbox_height - 1)

# Row index of scroll information line: Taking into account the zero-based
# row indexing and the command textbox area under the scroll information
# row.
self._output_scroll_row = self._max_y - 1 - self._command_textbox_height

# Tab completion bottom row.
self._candidates_top_row = self._output_scroll_row - 4
self._candidates_bottom_row = self._output_scroll_row - 1

# Maximum number of lines the candidates display can have.
self._candidates_max_lines = int(self._output_num_rows / 2)

self.max_output_lines = 10000

# Regex search state.
self._curr_search_regex = None
self._unwrapped_regex_match_lines = []

# Size of view port on screen, which is always smaller or equal to the
# screen size.
self._output_pad_screen_height = self._output_num_rows - 1
self._output_pad_screen_width = self._max_x - 2
self._output_pad_screen_location = self.rectangle(
    top=self._output_top_row,
    left=0,
    bottom=self._output_top_row + self._output_num_rows,
    right=self._output_pad_screen_width)
