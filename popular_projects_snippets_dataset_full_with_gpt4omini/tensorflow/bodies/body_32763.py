# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_inversion_test.py
# The matrix values do not effect auto-setting of the flags.
matrix = [[1., 0.], [1., 1.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix, is_positive_definite=False)
with self.assertRaisesRegex(ValueError, "positive-definite"):
    LinearOperatorInversion(operator, is_positive_definite=True)

operator = linalg.LinearOperatorFullMatrix(matrix, is_self_adjoint=False)
with self.assertRaisesRegex(ValueError, "self-adjoint"):
    LinearOperatorInversion(operator, is_self_adjoint=True)
