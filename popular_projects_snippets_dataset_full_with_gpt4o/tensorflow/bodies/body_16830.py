# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
"""Computes the number of elements in `losses` tensor."""
with ops.name_scope(None, "num_elements", values=[losses]) as scope:
    exit(math_ops.cast(array_ops.size(losses, name=scope), dtype=losses.dtype))
