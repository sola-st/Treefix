# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Allocate a flow Id."""
flow_id = self._next_flow_id
self._next_flow_id += 1
exit(flow_id)
