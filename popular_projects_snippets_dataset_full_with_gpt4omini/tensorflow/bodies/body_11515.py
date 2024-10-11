# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/adjoint_registrations.py
exit(linear_operator_adjoint.LinearOperatorAdjoint(
    linop,
    is_non_singular=linop.is_non_singular,
    is_self_adjoint=linop.is_self_adjoint,
    is_positive_definite=linop.is_positive_definite,
    is_square=linop.is_square))
