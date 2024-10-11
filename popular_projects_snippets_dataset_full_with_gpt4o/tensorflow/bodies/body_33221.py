# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
# The input should be invertible.
# The matrix is singular because it has a zero on the diagonal.
singular_matrix = np.array(
    [[[1., 0., 0.],
      [-1., 0., 0.],
      [0., -1., 1.]],
     [[1., 0., 0.],
      [-1., 1., 0.],
      [0., -1., 0.]],
     [[1., 0., 0.],
      [-1., 1., 0.],
      [0., -1., 1.]]])
rhs = np.array([[3.], [5.], [1.]])

expected = np.array([
    [[3.], [np.inf], [np.inf]],
    [[3.], [8.], [np.inf]],
    [[3.], [8.], [9.]]])

with self.cached_session(use_gpu=False):
    ans = linalg_ops.matrix_triangular_solve(singular_matrix, rhs)
    self.assertAllClose(self.evaluate(ans), expected)
