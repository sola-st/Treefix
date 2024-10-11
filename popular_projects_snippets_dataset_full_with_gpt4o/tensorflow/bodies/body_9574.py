# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Emits a record for a single counter.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      pid:  Identifier of the process generating this event as an integer.
      timestamp:  The timestamp of this event as a long integer.
      counter: Name of the counter as a string.
      value:  Value of the counter as an integer.
    """
event = self._create_event('C', category, name, pid, 0, timestamp)
event['args'] = {counter: value}
self._events.append(event)
