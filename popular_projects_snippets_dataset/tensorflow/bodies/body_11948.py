# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/inverse_registrations.py
exit(linear_operator_diag.LinearOperatorDiag(
    1. / diag_operator.diag,
    is_non_singular=diag_operator.is_non_singular,
    is_self_adjoint=diag_operator.is_self_adjoint,
    is_positive_definite=diag_operator.is_positive_definite,
    is_square=True))
