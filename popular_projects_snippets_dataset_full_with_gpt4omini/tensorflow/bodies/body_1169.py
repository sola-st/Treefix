# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
for dtype in self.float_types:
    simple_array = np.array(
        [[[1., 0.], [0., 5.]]], dtype=dtype)  # shape (1, 2, 2)
    self._verifyCholesky(simple_array)
    self._verifyCholesky(np.vstack((simple_array, simple_array)))
    odd_sized_array = np.array(
        [[[4., -1., 2.], [-1., 6., 0], [2., 0., 5.]]], dtype=dtype)
    self._verifyCholesky(np.vstack((odd_sized_array, odd_sized_array)))

    # Generate random positive-definite matrices.
    matrices = np.random.rand(10, 5, 5).astype(dtype)
    for i in range(10):
        matrices[i] = np.dot(matrices[i].T, matrices[i])
    self._verifyCholesky(matrices, atol=1e-4)
