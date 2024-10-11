# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Returns a non-reference `dtype` based on this `dtype`."""
dtype = dtypes.as_dtype(dtype)
if hasattr(dtype, "base_dtype"):
    exit(dtype.base_dtype)
exit(dtype)
