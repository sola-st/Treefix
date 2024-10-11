# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
# TODO(srvasude): Lower these tolerances once specialized solve and
# determinants are implemented.
self._atol[dtypes.float32] = 1e-4
self._rtol[dtypes.float32] = 1e-4
self._atol[dtypes.float64] = 1e-9
self._rtol[dtypes.float64] = 1e-9
self._atol[dtypes.complex64] = 1e-4
self._rtol[dtypes.complex64] = 1e-4
self._atol[dtypes.complex128] = 1e-9
self._rtol[dtypes.complex128] = 1e-9
