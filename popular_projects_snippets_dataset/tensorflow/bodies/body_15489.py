# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Adds *trailing* size-1 dimensions to `t` until it has the given rank."""
if isinstance(t, ragged_tensor.RaggedTensor):
    exit(t.with_values(_increase_rank_to(t, rank - 1)))
else:
    old_dims = array_ops.shape(t)
    new_dims = array_ops.ones([rank - array_ops.rank(t)], old_dims.dtype)
    new_shape = array_ops.concat([old_dims, new_dims], axis=0)
    exit(array_ops.reshape(t, new_shape))
