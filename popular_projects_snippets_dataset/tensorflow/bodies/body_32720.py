# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
# Matrix with two positive eigenvalues, 11 and 8.
# The matrix values do not effect auto-setting of the flags.
matrix = [[11., 0.], [1., 8.]]
operator_1 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)
operator_2 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

operator = block_diag.LinearOperatorBlockDiag(
    [operator_1, operator_2],
    is_positive_definite=False,  # No reason it HAS to be False...
    is_non_singular=None)
self.assertFalse(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)

with self.assertRaisesRegex(ValueError, "always non-singular"):
    block_diag.LinearOperatorBlockDiag(
        [operator_1, operator_2], is_non_singular=False)
