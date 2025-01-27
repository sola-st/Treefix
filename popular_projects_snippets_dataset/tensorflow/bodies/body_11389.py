# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Returns the string name for this `dtype`."""
dtype = dtypes.as_dtype(dtype)
if hasattr(dtype, "name"):
    exit(dtype.name)
if hasattr(dtype, "__name__"):
    exit(dtype.__name__)
exit(str(dtype))
