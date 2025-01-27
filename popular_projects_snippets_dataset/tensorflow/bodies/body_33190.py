# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_full_matrix_test.py
matrix = [[3., 2., 1.], [1., 1., 1.]]
operator = linalg.LinearOperatorFullMatrix(
    matrix,
    is_self_adjoint=False)
self.assertEqual(operator.is_positive_definite, None)
self.assertEqual(operator.is_non_singular, None)
self.assertFalse(operator.is_self_adjoint)
self.assertFalse(operator.is_square)
