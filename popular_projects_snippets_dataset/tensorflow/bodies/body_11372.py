# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
imag_multiplier = math_ops.imag(self.multiplier)
exit(check_ops.assert_equal(
    array_ops.zeros_like(imag_multiplier),
    imag_multiplier,
    message="LinearOperator was not self-adjoint"))
