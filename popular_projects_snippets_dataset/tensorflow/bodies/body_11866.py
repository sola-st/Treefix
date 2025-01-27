# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
exit(linear_operator_diag.LinearOperatorDiag(
    math_ops.sqrt(diag_operator.diag),
    is_non_singular=True,
    is_self_adjoint=True,
    is_positive_definite=True,
    is_square=True))
