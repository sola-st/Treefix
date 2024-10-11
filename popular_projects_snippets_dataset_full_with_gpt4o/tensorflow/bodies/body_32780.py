# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix = rng.randn(2, 3, 4)
operator = LinearOperatorMatmulSolve(matrix)
with self.cached_session():
    operator_dense = operator.to_dense()
    self.assertAllEqual((2, 3, 4), operator_dense.shape)
    self.assertAllClose(matrix, self.evaluate(operator_dense))
