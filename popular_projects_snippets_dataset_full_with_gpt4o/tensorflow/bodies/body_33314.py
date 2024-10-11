# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
matrix1 = np.array([[1., 2.], [3., 4.]])
matrix2 = np.array([[1., 3.], [3., 5.]])
matrix1 = matrix1.astype(np.complex64)
matrix1 += 1j * matrix1
matrix2 = matrix2.astype(np.complex64)
matrix2 += 1j * matrix2
self._verifyExponentialComplex(matrix1)
self._verifyExponentialComplex(matrix2)
# Complex batch
self._verifyExponentialComplex(self._makeBatch(matrix1, matrix2))
