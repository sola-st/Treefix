# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix = [[1., 0], [0., 2.]]
operator = LinearOperatorMatmulSolve(matrix)
y = [1., 1.]
with self.cached_session():
    x = operator.solvevec(y)
    self.assertAllEqual((2,), x.shape)
    self.assertAllClose([1., 1 / 2.], self.evaluate(x))
