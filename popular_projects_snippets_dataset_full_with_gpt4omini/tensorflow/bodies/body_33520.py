# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.cached_session():
    operator = linalg_lib.LinearOperatorScaledIdentity(
        num_rows=2, multiplier=[1., 2., 0.])
    with self.assertRaisesOpError("was singular"):
        self.evaluate(operator.assert_non_singular())
