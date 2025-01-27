# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
matrix = np.array([[1., 2.], [3., 4.]])
inv_matrix = np.linalg.inv(matrix)
x = np.array([1., 2.])
operator = linalg.LinearOperatorFullMatrix(matrix)
self.assertAllClose(inv_matrix.dot(x), self.evaluate(operator.solvevec(x)))
self.assertAllClose(
    inv_matrix.T.dot(x), self.evaluate(operator.H.solvevec(x)))
