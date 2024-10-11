# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
operator = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2,
    multiplier=3.,
    is_positive_definite=True,
    is_self_adjoint=True,
)
self.assertIsInstance(
    operator.cholesky(),
    linalg_lib.LinearOperatorScaledIdentity)
