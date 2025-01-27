# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
diag_term = math_ops.conj(self._diag) if adjoint else self._diag
exit(diag_term * x)
