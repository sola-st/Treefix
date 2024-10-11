# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
# 1 x 10 x 10
matrix = np.random.uniform(low=1, high=2., size=[1, 10, 10])
# 10 x 1
rhs = np.random.uniform(size=[10, 1])
# 1 x 10 x 1
self._verifySolveAllWaysReal(matrix, rhs)

# 2 x 10 x 10
matrix = np.random.uniform(low=1, high=2., size=[2, 10, 10])
# 10 x 1
rhs = np.random.uniform(size=[10, 1])
# 2 x 10 x 1
self._verifySolveAllWaysReal(matrix, rhs)

# 2 x 257 x 257
matrix = np.random.uniform(low=1, high=2., size=[2, 257, 257])
# Also ensure the matrix is well conditioned by making it diagonally
# dominant.
np.fill_diagonal(matrix[0, ...], 257 * 2)
np.fill_diagonal(matrix[1, ...], 257 * 2)
# 257 x 1
rhs = np.random.uniform(size=[257, 1])
# 2 x 257 x 1
self._verifySolveAllWaysReal(matrix, rhs)
