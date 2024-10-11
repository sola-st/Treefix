# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_inversion_test.py
# The matrix values do not effect auto-setting of the flags.
matrix = [[1., 0.], [1., 1.]]
operator = linalg.LinearOperatorFullMatrix(matrix)
operator_inv = LinearOperatorInversion(
    operator,
    is_positive_definite=True,
    is_non_singular=True,
    is_self_adjoint=False)
self.assertTrue(operator_inv.is_positive_definite)
self.assertTrue(operator_inv.is_non_singular)
self.assertFalse(operator_inv.is_self_adjoint)
