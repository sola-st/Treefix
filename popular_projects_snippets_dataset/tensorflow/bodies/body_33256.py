# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
with self.assertRaisesRegex(ValueError, "must be a list of >=1"):
    block_lower_triangular.LinearOperatorBlockLowerTriangular([])
