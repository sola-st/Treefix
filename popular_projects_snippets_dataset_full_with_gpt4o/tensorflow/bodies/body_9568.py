# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Adds a region event to the trace.

    Args:
      timestamp:  The start timestamp of this region as a long integer.
      duration:  The duration of this region as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      category: The event category as a string.
      name:  The event name as a string.
      args:  A JSON-compatible dictionary of event arguments.
    """
event = self._create_event('X', category, name, pid, tid, timestamp)
event['dur'] = duration
event['args'] = args
self._events.append(event)
