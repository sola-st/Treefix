# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
# 1x1 matrix, single rhs.
matrix = np.array([[0.1 + 1j * 0.1]])
rhs0 = np.array([[1. + 1j]])
self._verifySolveAllWaysComplex(matrix, rhs0)
# 2x2 matrices, single right-hand side.
matrix = np.array([[1., 2.], [3., 4.]]).astype(np.complex64)
matrix += 1j * matrix
rhs0 = np.array([[1.], [1.]]).astype(np.complex64)
rhs0 += 1j * rhs0
self._verifySolveAllWaysComplex(matrix, rhs0)
# 2x2 matrices, 3 right-hand sides.
rhs1 = np.array([[1., 0., 1.], [0., 1., 1.]]).astype(np.complex64)
rhs1 += 1j * rhs1
self._verifySolveAllWaysComplex(matrix, rhs1)
