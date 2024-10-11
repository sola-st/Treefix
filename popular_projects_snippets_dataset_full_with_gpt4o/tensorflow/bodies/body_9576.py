# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Formats the chrome trace to a string.

    Args:
      pretty: (Optional.)  If True, produce human-readable JSON output.

    Returns:
      A JSON-formatted string in Chrome Trace format.
    """
trace = {}
trace['traceEvents'] = self._metadata + self._events
if pretty:
    exit(json.dumps(trace, indent=4, separators=(',', ': ')))
else:
    exit(json.dumps(trace, separators=(',', ':')))
