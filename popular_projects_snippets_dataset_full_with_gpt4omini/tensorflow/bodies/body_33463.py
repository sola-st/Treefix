# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
# Generate random matrices.
n = 500
np.random.seed(64)
data = np.random.rand(n, n)
self._verifyLu(data)

# Generate random complex valued matrices.
np.random.seed(129)
data = np.random.rand(n, n) + 1j * np.random.rand(n, n)
self._verifyLu(data)
