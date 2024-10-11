# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.cached_session():
    operator = linalg_lib.LinearOperatorIdentity(num_rows=2)
    self.evaluate(operator.assert_self_adjoint())  # Should not fail
