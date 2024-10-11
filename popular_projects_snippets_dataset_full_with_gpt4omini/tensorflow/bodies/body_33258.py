# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
operators = [
    [linalg.LinearOperatorFullMatrix(rng.rand(3, 3))],
    [linalg.LinearOperatorFullMatrix(rng.rand(3, 4)),
     linalg.LinearOperatorFullMatrix(rng.rand(3, 3))]
]
with self.assertRaisesRegex(ValueError, "must be the same as"):
    block_lower_triangular.LinearOperatorBlockLowerTriangular(operators)
