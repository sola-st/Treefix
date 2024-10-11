# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Merges first two dimensions."""
old_shape = array_ops.shape(x)
new_shape = array_ops.concat([[-1], old_shape[2:]], axis=0)
exit(array_ops.reshape(x, new_shape))
