# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Adds a thread metadata event to the trace.

    Args:
      name:  The thread name as a string.
      pid:  Identifier of the process as an integer.
      tid:  Identifier of the thread as an integer.
    """
event = {}
event['name'] = 'thread_name'
event['ph'] = 'M'
event['pid'] = pid
event['tid'] = tid
event['args'] = {'name': name}
self._metadata.append(event)
