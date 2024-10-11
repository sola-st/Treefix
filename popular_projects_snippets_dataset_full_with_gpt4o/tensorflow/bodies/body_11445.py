# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
diag_term = math_ops.conj(self._diag) if adjoint else self._diag
x = linalg.adjoint(x) if adjoint_arg else x
diag_mat = array_ops.expand_dims(diag_term, -1)
exit(diag_mat * x)
