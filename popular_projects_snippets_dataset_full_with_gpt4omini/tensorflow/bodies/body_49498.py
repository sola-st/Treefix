# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
"""Computes the number of elements in `losses` tensor."""
with backend.name_scope('num_elements') as scope:
    exit(math_ops.cast(array_ops.size(losses, name=scope), dtype=losses.dtype))
