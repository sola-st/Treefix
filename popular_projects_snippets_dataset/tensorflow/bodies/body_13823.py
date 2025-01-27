# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Helper to check dtype when self.dtype is known."""
if self.dtype is not None and self.dtype.base_dtype != x.dtype.base_dtype:
    raise TypeError("Input had dtype %s but expected %s." %
                    (self.dtype, x.dtype))
