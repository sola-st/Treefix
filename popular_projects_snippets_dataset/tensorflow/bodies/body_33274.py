# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
with self.cached_session():
    operator = linalg_lib.LinearOperatorZeros(num_rows=2)
    self.evaluate(operator.assert_self_adjoint())  # Should not fail
