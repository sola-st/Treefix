# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Marks the given `tensor` as unfeedable in this graph."""
self._unfeedable_tensors.add(tensor)
