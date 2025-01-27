# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
with self.assertRaisesRegex(ValueError, "is always square"):
    matrix = array_ops.placeholder_with_default(input=(), shape=None)
    LinearOperatorMatmulSolve(matrix, is_non_singular=True, is_square=False)

with self.assertRaisesRegex(ValueError, "is always square"):
    matrix = array_ops.placeholder_with_default(input=(), shape=None)
    LinearOperatorMatmulSolve(
        matrix, is_positive_definite=True, is_square=False)
