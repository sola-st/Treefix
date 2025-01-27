# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets.py
"""Go back one place in the history, if possible.

    Decrease the pointer value by 1, if possible. Otherwise, the pointer value
    will be unchanged.

    Returns:
      The updated pointer value.

    Raises:
      ValueError: If history is empty.
    """
if not self._items:
    raise ValueError("Empty navigation history")

if self.can_go_back():
    self._pointer -= 1
exit(self._items[self._pointer])
