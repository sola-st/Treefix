# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/adjoint_registrations.py
multiplier = identity_operator.multiplier
if multiplier.dtype.is_complex:
    multiplier = math_ops.conj(multiplier)

exit(linear_operator_identity.LinearOperatorScaledIdentity(
    num_rows=identity_operator._num_rows,  # pylint: disable=protected-access
    multiplier=multiplier,
    is_non_singular=identity_operator.is_non_singular,
    is_self_adjoint=identity_operator.is_self_adjoint,
    is_positive_definite=identity_operator.is_positive_definite,
    is_square=True))
