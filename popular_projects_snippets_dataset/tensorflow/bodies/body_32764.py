# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_inversion_test.py
# The matrix values do not effect auto-setting of the flags.
matrix = [[1., 1.], [1., 1.]]

operator = linalg.LinearOperatorFullMatrix(matrix, is_non_singular=False)
with self.assertRaisesRegex(ValueError, "is_non_singular"):
    LinearOperatorInversion(operator)

operator = linalg.LinearOperatorFullMatrix(matrix)
with self.assertRaisesRegex(ValueError, "is_non_singular"):
    LinearOperatorInversion(operator, is_non_singular=False)
