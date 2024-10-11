# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
# A non-square matrix should cause an error.
matrix = np.array([[1., 2., 3.], [3., 4., 5.]])
with self.cached_session():
    with self.assertRaises(ValueError):
        self._verifySolve(matrix, matrix)
    with self.assertRaises(ValueError):
        self._verifySolve(matrix, matrix, batch_dims=[2, 3])
