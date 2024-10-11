# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
matrix = np.array([[1., 2.], [3., 4.]])
rhs = np.array([[1., 0., 1.], [0., 1., 1.]])
# Batch of 2x3x2x2 matrices, 2x3x2x3 right-hand sides.
self._verifySolveAllWaysReal(matrix, rhs, batch_dims=[2, 3])
# Batch of 3x2x2x2 matrices, 3x2x2x3 right-hand sides.
self._verifySolveAllWaysReal(matrix, rhs, batch_dims=[3, 2])

matrix = np.array([[1., 2., 3., 4.], [-1., -2., -3., -4.],
                   [-1., 1., 2., 3.]])
rhs = np.array([[-1., 2.], [1., 1.], [0., 1.], [2., 3.]])
# Batch of 2x3x4x4 matrices with 3 bands, 2x3x4x2 right-hand sides.
self._verifySolveAllWaysReal(matrix, rhs, batch_dims=[2, 3])
# Batch of 3x2x4x4 matrices with 3 bands, 3x2x4x2 right-hand sides.
self._verifySolveAllWaysReal(matrix, rhs, batch_dims=[3, 2])
