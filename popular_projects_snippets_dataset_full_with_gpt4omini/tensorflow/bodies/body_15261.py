# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Broadcast from 1 element to target_size elements."""
exit(_LayerBroadcaster.from_gather_index(
    array_ops.zeros(target_size, dtype=target_size.dtype)))
