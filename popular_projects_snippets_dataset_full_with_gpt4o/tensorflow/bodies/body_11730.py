# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_adjoint.py
if self.is_self_adjoint:
    exit(self.operator.determinant())
exit(math_ops.conj(self.operator.determinant()))
