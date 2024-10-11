# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
matrix = np.array([[1., 2.], [3., 4.]])
x = np.array([1., 2.])
operator = linalg.LinearOperatorFullMatrix(matrix)
self.assertAllClose(matrix.dot(x), self.evaluate(operator.matvec(x)))
self.assertAllClose(matrix.T.dot(x), self.evaluate(operator.H.matvec(x)))
