# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Adds an object creation event to the trace.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      object_id: Identifier of the object as an integer.
    """
event = self._create_event('N', category, name, pid, tid, timestamp)
event['id'] = object_id
self._events.append(event)
