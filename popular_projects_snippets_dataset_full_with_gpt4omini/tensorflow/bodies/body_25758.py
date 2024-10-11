# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets.py
"""Add an item to the navigation histoyr.

    Args:
      command: command line text.
      screen_output: screen output produced for the command.
      scroll_position: (`int`) scroll position in the screen output.
    """
if self._pointer + 1 < len(self._items):
    self._items = self._items[:self._pointer + 1]
self._items.append(
    NavigationHistoryItem(command, screen_output, scroll_position))
if len(self._items) > self._capacity:
    self._items = self._items[-self._capacity:]
self._pointer = len(self._items) - 1
