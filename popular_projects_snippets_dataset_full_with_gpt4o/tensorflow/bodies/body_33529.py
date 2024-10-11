# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
operator = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2, multiplier=1.,
    is_positive_definite=False, is_non_singular=True)
self.assertFalse(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)
self.assertTrue(operator.is_self_adjoint)  # Auto-set due to real multiplier
