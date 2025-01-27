# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_inverse_op_test.py
# 2x2 matrices
matrix1 = np.array([[2., 1.], [1., 2.]])
matrix2 = np.array([[3., -1.], [-1., 3.]])
self._verifyInverseReal(matrix1)
self._verifyInverseReal(matrix2)
# A multidimensional batch of 2x2 matrices
self._verifyInverseReal(self._makeBatch(matrix1, matrix2))
