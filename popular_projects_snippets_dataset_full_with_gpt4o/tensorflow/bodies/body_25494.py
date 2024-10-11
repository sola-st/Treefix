# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
nav_bar_width = self._max_x - 2
self._nav_bar_pad = self._screen_new_output_pad(1, nav_bar_width)
self._nav_bar = self._nav_history.render(
    nav_bar_width,
    self._NAVIGATION_BACK_COMMAND,
    self._NAVIGATION_FORWARD_COMMAND)
self._screen_add_line_to_output_pad(
    self._nav_bar_pad, 0, self._nav_bar.lines[0][:nav_bar_width - 1],
    color_segments=(self._nav_bar.font_attr_segs[0]
                    if 0 in self._nav_bar.font_attr_segs else None))
