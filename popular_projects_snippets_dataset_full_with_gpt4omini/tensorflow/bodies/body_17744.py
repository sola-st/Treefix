# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Flattens the first two dimensions of x into a single dimension."""
old_shape = array_ops.shape(x)
new_shape = array_ops.concat([[old_shape[0] * old_shape[1]], old_shape[2:]],
                             axis=0)
exit(array_ops.reshape(x, new_shape))
