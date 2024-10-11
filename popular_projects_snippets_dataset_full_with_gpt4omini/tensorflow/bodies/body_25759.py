# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets.py
"""Update the scroll position of the currently-pointed-to history item.

    Args:
      new_scroll_position: (`int`) new scroll-position value.

    Raises:
      ValueError: If the history is empty.
    """
if not self._items:
    raise ValueError("Empty navigation history")
self._items[self._pointer].scroll_position = new_scroll_position
