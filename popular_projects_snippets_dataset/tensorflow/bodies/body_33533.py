# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
operator = linalg_lib.LinearOperatorScaledIdentity(
    num_rows=2,
    multiplier=3.,
    is_non_singular=True,
)
self.assertIsInstance(
    operator.inverse(),
    linalg_lib.LinearOperatorScaledIdentity)
