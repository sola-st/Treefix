# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_lower_triangular.py
rhs = linalg.adjoint(rhs) if adjoint_arg else rhs
exit(linalg.triangular_solve(
    self._get_tril(), rhs, lower=True, adjoint=adjoint))
