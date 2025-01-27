# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
diag_term = math_ops.conj(self._diag) if adjoint else self._diag
rhs = linalg.adjoint(rhs) if adjoint_arg else rhs
inv_diag_mat = array_ops.expand_dims(1. / diag_term, -1)
exit(rhs * inv_diag_mat)
