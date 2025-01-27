# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
# The input should be invertible.
# The matrix is singular because it has a zero on the diagonal.
# FIXME(rmlarsen): The GPU kernel does not check for singularity.
singular_matrix = np.array([[1., 0., -1.], [-1., 0., 1.], [0., -1., 1.]])
with self.cached_session():
    with self.assertRaisesOpError("Input matrix is not invertible."):
        self._verifySolve(singular_matrix, singular_matrix)
    with self.assertRaisesOpError("Input matrix is not invertible."):
        self._verifySolve(singular_matrix, singular_matrix, batch_dims=[2, 3])
