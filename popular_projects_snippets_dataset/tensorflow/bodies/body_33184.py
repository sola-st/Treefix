# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
# Matrix with two positive eigenvalues.
matrix = [[1., 0.], [0., 7.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix, is_positive_definite=True, is_self_adjoint=True)

self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_self_adjoint)

# Should be auto-set
self.assertTrue(operator.is_non_singular)
self.assertTrue(operator._can_use_cholesky)
self.assertTrue(operator.is_square)
