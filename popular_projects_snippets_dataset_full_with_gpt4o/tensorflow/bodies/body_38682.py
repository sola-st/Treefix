# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
# The matrix should have the same number of rows as the
# right-hand sides.
matrix = np.array([[1., 1.], [1., 1.]])
rhs = np.array([[1., 0.]])
with self.cached_session():
    with self.assertRaises(ValueError):
        self._verifySolve(matrix, rhs)
    with self.assertRaises(ValueError):
        self._verifySolve(matrix, rhs, batch_dims=[2, 3])

    # Number of bands exceeds the dimension of the matrix.
matrix = np.ones((6, 4))
rhs = np.ones((4, 2))
with self.cached_session():
    with self.assertRaises(ValueError):
        self._verifySolve(matrix, rhs)
    with self.assertRaises(ValueError):
        self._verifySolve(matrix, rhs, batch_dims=[2, 3])
