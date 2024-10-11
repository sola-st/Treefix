# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Adds a process metadata event to the trace.

    Args:
      name:  The process name as a string.
      pid:  Identifier of the process as an integer.
    """
event = {}
event['name'] = 'process_name'
event['ph'] = 'M'
event['pid'] = pid
event['args'] = {'name': name}
self._metadata.append(event)
