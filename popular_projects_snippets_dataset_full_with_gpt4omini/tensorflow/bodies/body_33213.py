# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
# 1x1 matrix, single rhs.
matrix = np.array([[0.1]])
rhs0 = np.array([[1.]])
self._verifySolveAllWaysReal(matrix, rhs0)
# 2x2 matrices, single right-hand side.
matrix = np.array([[1., 2.], [3., 4.]])
rhs0 = np.array([[1.], [1.]])
self._verifySolveAllWaysReal(matrix, rhs0)
# 2x2 matrices, 3 right-hand sides.
rhs1 = np.array([[1., 0., 1.], [0., 1., 1.]])
self._verifySolveAllWaysReal(matrix, rhs1)
