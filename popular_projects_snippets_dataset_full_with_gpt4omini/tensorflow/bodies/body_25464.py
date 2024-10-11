# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Initialization of screen colors."""
curses.start_color()
curses.use_default_colors()
self._color_pairs = {}
color_index = 0

# Prepare color pairs.
for fg_color in self._FOREGROUND_COLORS:
    for bg_color in self._BACKGROUND_COLORS:
        color_index += 1
        curses.init_pair(color_index, self._FOREGROUND_COLORS[fg_color],
                         self._BACKGROUND_COLORS[bg_color])

        color_name = fg_color
        if bg_color != "transparent":
            color_name += "_on_" + bg_color

        self._color_pairs[color_name] = curses.color_pair(color_index)

    # Try getting color(s) available only under 256-color support.
try:
    color_index += 1
    curses.init_pair(color_index, 245, -1)
    self._color_pairs[cli_shared.COLOR_GRAY] = curses.color_pair(color_index)
except curses.error:
    # Use fall-back color(s):
    self._color_pairs[cli_shared.COLOR_GRAY] = (
        self._color_pairs[cli_shared.COLOR_GREEN])

# A_BOLD or A_BLINK is not really a "color". But place it here for
# convenience.
self._color_pairs["bold"] = curses.A_BOLD
self._color_pairs["blink"] = curses.A_BLINK
self._color_pairs["underline"] = curses.A_UNDERLINE

# Default color pair to use when a specified color pair does not exist.
self._default_color_pair = self._color_pairs[cli_shared.COLOR_WHITE]
