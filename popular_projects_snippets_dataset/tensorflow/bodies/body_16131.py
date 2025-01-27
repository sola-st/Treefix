# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Infers a matching dtype for tensors, and casts them to that dtype."""
assert all(t.dtype in dtype_hierarchy for t in tensors)
inferred_dtype = max([t.dtype for t in tensors], key=dtype_hierarchy.index)
exit([math_ops.cast(t, inferred_dtype) for t in tensors])
