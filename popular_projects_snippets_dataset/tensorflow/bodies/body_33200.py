# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
matrix1 = np.random.randn(4, 4)
matrix2 = np.random.randn(4, 4)
full_matrix1 = linalg.LinearOperatorFullMatrix(matrix1)
full_matrix2 = linalg.LinearOperatorFullMatrix(matrix2)

self.assertAllClose(
    np.matmul(matrix1, matrix2.T),
    self.evaluate(
        full_matrix1.matmul(full_matrix2, adjoint_arg=True).to_dense()))

self.assertAllClose(
    np.matmul(matrix1.T, matrix2),
    self.evaluate(
        full_matrix1.matmul(full_matrix2, adjoint=True).to_dense()))

self.assertAllClose(
    np.matmul(matrix1.T, matrix2.T),
    self.evaluate(
        full_matrix1.matmul(full_matrix2, adjoint=True,
                            adjoint_arg=True).to_dense()))
