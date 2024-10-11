# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
# The matrix values do not effect auto-setting of the flags.
matrix = [[1., 0.], [1., 1.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix,
    is_positive_definite=True,
    is_non_singular=True,
    is_self_adjoint=False)
operator_adjoint = LinearOperatorAdjoint(operator)
self.assertTrue(operator_adjoint.is_positive_definite)
self.assertTrue(operator_adjoint.is_non_singular)
self.assertFalse(operator_adjoint.is_self_adjoint)
