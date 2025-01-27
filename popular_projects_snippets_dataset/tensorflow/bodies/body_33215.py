# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
matrix = np.array([[1., 2.], [3., 4.]])
rhs = np.array([[1., 0., 1.], [0., 1., 1.]])
# Batch of 2x3x2x2 matrices, 2x3x2x3 right-hand sides.
self._verifySolveAllWaysReal(matrix, rhs, batch_dims=[2, 3])
# Batch of 3x2x2x2 matrices, 3x2x2x3 right-hand sides.
self._verifySolveAllWaysReal(matrix, rhs, batch_dims=[3, 2])
