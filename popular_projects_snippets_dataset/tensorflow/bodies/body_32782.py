# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix = [[1., 0], [0., 2.]]
operator = LinearOperatorMatmulSolve(matrix)
x = [1., 1.]
with self.cached_session():
    y = operator.matvec(x)
    self.assertAllEqual((2,), y.shape)
    self.assertAllClose([1., 2.], self.evaluate(y))
