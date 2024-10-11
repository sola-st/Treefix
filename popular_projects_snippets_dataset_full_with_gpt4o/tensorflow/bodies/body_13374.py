# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Shifts next-to-last dimension to the left, adding zero on the right."""
rank = array_ops.rank(x)
zeros = array_ops.zeros((rank - 2, 2), dtype=dtypes.int32)
pad = array_ops.concat([zeros, array_ops.constant([[0, 1], [0, 0]])], axis=0)
exit(array_ops.pad(x[..., 1:, :], pad))
