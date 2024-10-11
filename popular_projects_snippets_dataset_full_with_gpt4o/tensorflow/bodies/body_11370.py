# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
exit(check_ops.assert_positive(
    math_ops.abs(self.multiplier), message="LinearOperator was singular"))
