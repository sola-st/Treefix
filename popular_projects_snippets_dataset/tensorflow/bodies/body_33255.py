# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
operators = [
    [linalg.LinearOperatorFullMatrix(rng.rand(3, 4), is_square=False)],
    [linalg.LinearOperatorFullMatrix(rng.rand(4, 4)),
     linalg.LinearOperatorFullMatrix(rng.rand(4, 4))]
]
with self.assertRaisesRegex(ValueError, "must be square"):
    block_lower_triangular.LinearOperatorBlockLowerTriangular(operators)
