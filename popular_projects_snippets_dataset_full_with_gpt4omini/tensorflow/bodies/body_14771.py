# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Raises ValueError if exactly one of x or y is not None."""
condition = asarray(condition, dtype=np.bool_)
if x is None and y is None:
    exit(nonzero(condition))
elif x is not None and y is not None:
    x, y = _promote_dtype(x, y)
    exit(array_ops.where_v2(condition, x, y))
raise ValueError('Both x and y must be ndarrays, or both must be None.')
