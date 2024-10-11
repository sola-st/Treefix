# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
# Real
self._verifySquareRootReal(matrix1)
self._verifySquareRootReal(matrix2)
self._verifySquareRootReal(self._makeBatch(matrix1, matrix2))
matrix1 = matrix1.astype(np.complex64)
matrix2 = matrix2.astype(np.complex64)
matrix1 += 1j * matrix1
matrix2 += 1j * matrix2
self._verifySquareRootComplex(matrix1)
self._verifySquareRootComplex(matrix2)
self._verifySquareRootComplex(self._makeBatch(matrix1, matrix2))
