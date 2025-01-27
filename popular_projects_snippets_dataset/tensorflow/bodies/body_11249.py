# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""Derived classes can set _atol, _rtol to get different tolerance."""
dtype = dtypes.as_dtype(x.dtype)
atol = self._atol[dtype]
rtol = self._rtol[dtype]
self.assertAllClose(x, y, atol=atol, rtol=rtol)
if check_dtype:
    self.assertDTypeEqual(x, y.dtype)
