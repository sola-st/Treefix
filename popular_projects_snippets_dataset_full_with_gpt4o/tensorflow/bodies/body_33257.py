# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
with self.assertRaisesRegex(ValueError, "must contain `2` blocks"):
    block_lower_triangular.LinearOperatorBlockLowerTriangular([
        [linalg.LinearOperatorFullMatrix(rng.rand(2, 2))],
        [linalg.LinearOperatorFullMatrix(rng.rand(2, 2))
         for _ in range(3)]])
