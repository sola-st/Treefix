# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Check that arg.dtype == self.dtype."""
if arg.dtype.base_dtype != dtype:
    raise TypeError(
        f"Expected argument to have dtype {dtype}. Found: {arg.dtype} in "
        f"tensor {arg}.")
