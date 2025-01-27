# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
matrix1 = np.array([[2., 1.], [1., 2.]])
matrix2 = np.array([[3., -1.], [-1., 3.]])
self._testMatrices(matrix1, matrix2)
