# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
# 2 x 2 x 2
matrix = np.array([[[1., 0.], [3., 4.]], [[1., 0.], [2., 1.]]])
# 2 x 3
rhs = np.array([[1., 0., 1.], [0., 1., 1.]])
# 2 x 2 x 3
self._verifySolveAllWaysReal(matrix, rhs)
# 2 x 2 x 2
matrix2 = np.array([[[1., 0.], [3., 4.]], [[2., 0.], [1., 6.3]]])
# 1 x 2 x 3
rhs = np.array([[[1., 0., 1.], [0., 1., 1.]]])
# 2 x 2 x 3
self._verifySolveAllWaysReal(matrix2, rhs)
