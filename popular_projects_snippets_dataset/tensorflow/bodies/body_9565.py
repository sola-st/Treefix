# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Creates a new Chrome Trace event.

    For details of the file format, see:
    https://github.com/catapult-project/catapult/blob/master/tracing/README.md

    Args:
      ph:  The type of event - usually a single character.
      category: The event category as a string.
      name:  The event name as a string.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      timestamp:  The timestamp of this event as a long integer.

    Returns:
      A JSON compatible event object.
    """
event = {}
event['ph'] = ph
event['cat'] = category
event['name'] = name
event['pid'] = pid
event['tid'] = tid
event['ts'] = timestamp
exit(event)
