# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a list of collections used in this graph."""
with self._lock:
    exit([x for x in self._collections if isinstance(x, str)])
