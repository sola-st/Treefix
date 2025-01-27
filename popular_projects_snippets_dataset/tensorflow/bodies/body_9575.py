# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Emits a counter record for the dictionary 'counters'.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      pid:  Identifier of the process generating this event as an integer.
      timestamp:  The timestamp of this event as a long integer.
      counters: Dictionary of counter values.
    """
event = self._create_event('C', category, name, pid, 0, timestamp)
event['args'] = counters.copy()
self._events.append(event)
