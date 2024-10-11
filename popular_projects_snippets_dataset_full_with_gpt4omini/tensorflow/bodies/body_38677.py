# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
# 1x1 matrix, single rhs.
matrix = np.array([[0.1]])
rhs0 = np.array([[1.]])
self._verifySolveAllWaysReal(matrix, rhs0)
# 2x2 matrix with 2 bands, single right-hand side.
# Corresponds to the lower triangular
# [[1., 0.], [3., 4.]]
# and upper triangular
# [[2., 1.], [0., 3.]]
matrix = np.array([[1., 4.], [2., 3.]])
rhs0 = np.array([[1.], [1.]])
self._verifySolveAllWaysReal(matrix, rhs0)
# 2x2 matrix with 2 bands, 3 right-hand sides.
rhs1 = np.array([[1., 0., 1.], [0., 1., 1.]])
self._verifySolveAllWaysReal(matrix, rhs1)
# 4 x 4 matrix with 2 bands, 3 right hand sides.
# Corresponds to the lower triangular
# [[1.,  0., 0., 0.],
#  [-1., 2., 0., 0.],
#  [0., -2., 3., 0.],
#  [0., 0., -3., 4.]]
# and upper triangular
# [[1.,  1., 0., 0.],
#  [0., -1., 2., 0.],
#  [0., 0., -2., 3.],
#  [0., 0., 0., -3.]]
matrix = np.array([[1., 2., 3., 4.], [1., -1., -2., -3.]])
rhs0 = np.array([[1., 0., 1.], [0., 1., 1.], [-1., 2., 1.], [0., -1., -1.]])
self._verifySolveAllWaysReal(matrix, rhs0)
