# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
operator = linalg_lib.LinearOperatorIdentity(
    num_rows=2, is_non_singular=True)
self.assertIsInstance(
    operator.adjoint(), linalg_lib.LinearOperatorIdentity)
