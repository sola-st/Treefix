# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
# Matrix with two positive eigenvalues, 11 and 8.
# The matrix values do not effect auto-setting of the flags.
matrix = [[11., 0.], [1., 8.]]
operator_1 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)
operator_2 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)
operator_3 = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=True)

operator = block_lower_triangular.LinearOperatorBlockLowerTriangular(
    [[operator_1], [operator_2, operator_3]],
    is_positive_definite=False,  # No reason it HAS to be False...
    is_non_singular=None)
self.assertFalse(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)

with self.assertRaisesRegex(ValueError, "always non-singular"):
    block_lower_triangular.LinearOperatorBlockLowerTriangular(
        [[operator_1], [operator_2, operator_3]], is_non_singular=False)

operator_4 = linalg.LinearOperatorFullMatrix(
    [[1., 0.], [2., 0.]], is_non_singular=False)

# A singular operator off of the main diagonal shouldn't raise
block_lower_triangular.LinearOperatorBlockLowerTriangular(
    [[operator_1], [operator_4, operator_2]], is_non_singular=True)

with self.assertRaisesRegex(ValueError, "always singular"):
    block_lower_triangular.LinearOperatorBlockLowerTriangular(
        [[operator_1], [operator_2, operator_4]], is_non_singular=True)
