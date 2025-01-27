# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
operator = LinearOperatorShape(
    shape=(2, 2),
    is_non_singular=False,
    is_self_adjoint=True,
    is_positive_definite=False)
self.assertFalse(operator.is_non_singular)
self.assertTrue(operator.is_self_adjoint)
self.assertFalse(operator.is_positive_definite)
