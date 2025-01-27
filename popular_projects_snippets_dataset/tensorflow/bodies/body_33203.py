# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
matrix1 = self.evaluate(
    linear_operator_test_util.random_tril_matrix(
        [4, 4], dtype=dtypes.float64, force_well_conditioned=True))
matrix2 = np.random.randn(4, 4)
full_matrix1 = linalg.LinearOperatorLowerTriangular(
    matrix1, is_non_singular=True)
full_matrix2 = linalg.LinearOperatorFullMatrix(matrix2)

self.assertAllClose(
    self.evaluate(linalg.triangular_solve(matrix1, matrix2.T)),
    self.evaluate(
        full_matrix1.solve(full_matrix2, adjoint_arg=True).to_dense()))

self.assertAllClose(
    self.evaluate(linalg.triangular_solve(matrix1.T, matrix2, lower=False)),
    self.evaluate(
        full_matrix1.solve(full_matrix2, adjoint=True).to_dense()))

self.assertAllClose(
    self.evaluate(
        linalg.triangular_solve(matrix1.T, matrix2.T, lower=False)),
    self.evaluate(
        full_matrix1.solve(full_matrix2, adjoint=True,
                           adjoint_arg=True).to_dense()))
