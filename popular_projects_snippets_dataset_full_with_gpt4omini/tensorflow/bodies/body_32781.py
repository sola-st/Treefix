# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
matrix = rng.randn(2, 3, 4)
matrix_ph = array_ops.placeholder_with_default(input=matrix, shape=None)
operator = LinearOperatorMatmulSolve(matrix_ph)
operator_dense = operator.to_dense()
self.assertAllClose(matrix, self.evaluate(operator_dense))
