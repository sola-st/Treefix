# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Conditionally store a single sparse Tensor."""
exit(utils.smart_cond(
    keep_input,
    lambda: _store_sparse(t, shared_name=map_op_name),
    lambda: constant_op.constant(-1, dtypes.int64)))
