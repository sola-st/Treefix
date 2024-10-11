# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Splits first dimension into [first_dim, -1]."""
old_shape = array_ops.shape(x)
new_shape = array_ops.concat([first_dim, [-1], old_shape[1:]], axis=0)
exit(array_ops.reshape(x, new_shape))
