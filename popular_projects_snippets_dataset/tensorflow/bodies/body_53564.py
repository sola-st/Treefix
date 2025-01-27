# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Marks the given `op` as unfetchable in this graph."""
self._unfetchable_ops.add(op)
