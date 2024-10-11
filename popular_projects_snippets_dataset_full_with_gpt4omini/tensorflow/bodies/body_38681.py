# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
matrix = np.array([[1., 2.], [3., 4.]]).astype(np.complex64)
matrix += 1j * matrix
rhs = np.array([[1., 0., 1.], [0., 1., 1.]]).astype(np.complex64)
rhs += 1j * rhs
# Batch of 2x3x2x2 matrices, 2x3x2x3 right-hand sides.
self._verifySolveAllWaysComplex(matrix, rhs, batch_dims=[2, 3])
# Batch of 3x2x2x2 matrices, 3x2x2x3 right-hand sides.
self._verifySolveAllWaysComplex(matrix, rhs, batch_dims=[3, 2])
