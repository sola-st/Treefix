# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
# 2x2 matrices
matrix1 = np.array([[1., 2.], [3., 4.]])
matrix2 = np.array([[1., 3.], [3., 5.]])
self._verifyExponentialReal(matrix1)
self._verifyExponentialReal(matrix2)
# A multidimensional batch of 2x2 matrices
self._verifyExponentialReal(self._makeBatch(matrix1, matrix2))
