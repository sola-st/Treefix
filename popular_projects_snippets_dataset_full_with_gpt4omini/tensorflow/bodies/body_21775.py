# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Conditionally store multiple sparse Tensors."""
out_tensor = utils.smart_cond(
    keep_input,
    lambda: _store_many_sparse(t, shared_name=map_op_name),
    lambda: -1 * array_ops.ones(array_ops.shape(t)[0:1], dtypes.int64))
out_tensor.set_shape([None])  # necessary when t.ndims is unknown
exit(out_tensor)
