# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
simple_array = np.array([[[1., 0.], [0., 5.]]])  # shape (1, 2, 2)
self._verifyCholesky(simple_array)
self._verifyCholesky(np.vstack((simple_array, simple_array)))
odd_sized_array = np.array([[[4., -1., 2.], [-1., 6., 0], [2., 0., 5.]]])
self._verifyCholesky(np.vstack((odd_sized_array, odd_sized_array)))

# Generate random positive-definite matrices.
matrices = np.random.rand(10, 5, 5)
for i in range(10):
    with self.subTest(i=i):
        matrices[i] = np.dot(matrices[i].T, matrices[i])
self._verifyCholesky(matrices)

# Generate random complex valued positive-definite matrices.
matrices = np.random.rand(10, 5, 5) + 1j * np.random.rand(10, 5, 5)
for i in range(10):
    with self.subTest(i=i):
        matrices[i] = np.dot(matrices[i].T.conj(), matrices[i])
self._verifyCholesky(matrices)
