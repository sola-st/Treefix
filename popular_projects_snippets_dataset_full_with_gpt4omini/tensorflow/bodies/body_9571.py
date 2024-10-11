# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Adds an object snapshot event to the trace.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      object_id: Identifier of the object as an integer.
      snapshot:  A JSON-compatible representation of the object.
    """
event = self._create_event('O', category, name, pid, tid, timestamp)
event['id'] = object_id
event['args'] = {'snapshot': snapshot}
self._events.append(event)
