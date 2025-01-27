# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_adjoint.py
eigvals = self.operator.eigvals()
if not self.operator.is_self_adjoint:
    eigvals = math_ops.conj(eigvals)
exit(eigvals)
