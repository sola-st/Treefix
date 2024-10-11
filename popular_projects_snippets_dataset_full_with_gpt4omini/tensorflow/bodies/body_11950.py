# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/inverse_registrations.py
exit(linear_operator_identity.LinearOperatorScaledIdentity(
    num_rows=identity_operator._num_rows,  # pylint: disable=protected-access
    multiplier=1. / identity_operator.multiplier,
    is_non_singular=identity_operator.is_non_singular,
    is_self_adjoint=True,
    is_positive_definite=identity_operator.is_positive_definite,
    is_square=True))
