# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
# Matrix with two positive eigenvalues.
matrix = [[1., 0.], [1., 11.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix,
    is_positive_definite=True,
    is_non_singular=True,
    is_self_adjoint=False)
self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)
self.assertFalse(operator.is_self_adjoint)
# Auto-detected.
self.assertTrue(operator.is_square)
