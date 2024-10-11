# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Check that arg.dtype == self.dtype."""
if arg.dtype.base_dtype != self.dtype:
    raise TypeError(
        "Expected argument to have dtype %s.  Found: %s in tensor %s" %
        (self.dtype, arg.dtype, arg))
