# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
simple_array = np.array([[[1., -1.], [2., 5.]]])  # shape (1, 2, 2)
self._verifyLu(simple_array)
self._verifyLu(np.vstack((simple_array, simple_array)))
odd_sized_array = np.array([[[4., -1., 2.], [-1., 6., 0], [2., 0., 5.]]])
self._verifyLu(np.vstack((odd_sized_array, odd_sized_array)))

batch_size = 200

# Generate random matrices.
np.random.seed(42)
matrices = np.random.rand(batch_size, 5, 5)
self._verifyLu(matrices)

# Generate random complex valued matrices.
np.random.seed(52)
matrices = np.random.rand(batch_size, 5,
                          5) + 1j * np.random.rand(batch_size, 5, 5)
self._verifyLu(matrices)
