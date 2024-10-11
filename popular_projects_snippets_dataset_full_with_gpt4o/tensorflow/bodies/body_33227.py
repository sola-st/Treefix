# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
# Matrix with two positive eigenvalues, 1, and 1.
# The matrix values do not effect auto-setting of the flags.
matrix = [[1., 0.], [1., 1.]]
operator = linalg.LinearOperatorComposition(
    [linalg.LinearOperatorFullMatrix(matrix)],
    is_positive_definite=True,
    is_non_singular=True,
    is_self_adjoint=False)
self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)
self.assertFalse(operator.is_self_adjoint)
