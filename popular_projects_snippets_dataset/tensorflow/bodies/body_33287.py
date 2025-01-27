# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
# The is_x flags are by default all True.
operator = linalg_lib.LinearOperatorZeros(num_rows=2)
self.assertFalse(operator.is_positive_definite)
self.assertFalse(operator.is_non_singular)
self.assertTrue(operator.is_self_adjoint)
