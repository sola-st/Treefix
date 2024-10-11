# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets.py
"""Constructor of CursesNavigationHistory.

    Args:
      capacity: (`int`) How many items this object can hold. Each item consists
        of a command stirng, an output RichTextLines object and a scroll
        position.

    Raises:
      ValueError: If capacity is not a positive number.
    """
if capacity <= 0:
    raise ValueError("In valid capacity value: %d" % capacity)

self._capacity = capacity
self._items = []
self._pointer = -1
