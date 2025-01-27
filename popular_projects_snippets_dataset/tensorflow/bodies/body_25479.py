# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Navigate in screen output history.

    Args:
      command: (`str`) the navigation command, from
        {self._NAVIGATION_FORWARD_COMMAND, self._NAVIGATION_BACK_COMMAND}.
    """
if command == self._NAVIGATION_FORWARD_COMMAND:
    if self._nav_history.can_go_forward():
        item = self._nav_history.go_forward()
        scroll_position = item.scroll_position
    else:
        self._toast("At the LATEST in navigation history!",
                    color=self._NAVIGATION_WARNING_COLOR_PAIR)
        exit()
else:
    if self._nav_history.can_go_back():
        item = self._nav_history.go_back()
        scroll_position = item.scroll_position
    else:
        self._toast("At the OLDEST in navigation history!",
                    color=self._NAVIGATION_WARNING_COLOR_PAIR)
        exit()

self._display_output(item.screen_output)
if scroll_position != 0:
    self._scroll_output(_SCROLL_TO_LINE_INDEX, line_index=scroll_position)
