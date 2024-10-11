from typing import List, Dict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._events = [] # pragma: no cover
self._create_event = lambda event_type, category, name, pid, tid, timestamp: {'type': event_type, 'category': category, 'name': name, 'pid': pid, 'tid': tid, 'timestamp': timestamp} # pragma: no cover
name = 'DataFlowStart' # pragma: no cover
pid = 1234 # pragma: no cover
tid = 5678 # pragma: no cover
timestamp = 1691234567890 # pragma: no cover
flow_id = 42 # pragma: no cover

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
