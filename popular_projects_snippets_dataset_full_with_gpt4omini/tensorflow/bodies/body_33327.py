# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
np.random.seed(42)
matrix = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype)
l1_norm = np.max(np.sum(np.abs(matrix), axis=matrix.ndim - 2))
matrix /= l1_norm
self._verifyExponentialReal(scale * matrix)
