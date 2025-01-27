# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
# Increase from 1e-6 to 1e-5.  This reduction in tolerance happens,
# presumably, because we are taking a different code path in the operator
# and the matrix.  The operator uses a Cholesky, the matrix uses standard
# solve.
self._atol[dtypes.float32] = 1e-5
self._rtol[dtypes.float32] = 1e-5
self._atol[dtypes.float64] = 1e-10
self._rtol[dtypes.float64] = 1e-10
