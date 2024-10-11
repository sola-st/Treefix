# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
from l3.Runtime import _l_
"""Adds a flow start event to the trace.

    When matched with a flow end event (with the same 'flow_id') this will
    cause the trace viewer to draw an arrow between the start and end events.

    Args:
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      flow_id: Identifier of the flow as an integer.
    """
event = self._create_event('s', 'DataFlow', name, pid, tid, timestamp)
_l_(9258)
event['id'] = flow_id
_l_(9259)
self._events.append(event)
_l_(9260)
