# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
exit(linear_operator_identity.LinearOperatorScaledIdentity(
    num_rows=identity_operator._num_rows,  # pylint: disable=protected-access
    multiplier=math_ops.sqrt(identity_operator.multiplier),
    is_non_singular=True,
    is_self_adjoint=True,
    is_positive_definite=True,
    is_square=True))
