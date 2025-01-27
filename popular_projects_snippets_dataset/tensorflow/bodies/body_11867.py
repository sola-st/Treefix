# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
exit(linear_operator_identity.LinearOperatorIdentity(
    num_rows=identity_operator._num_rows,  # pylint: disable=protected-access
    batch_shape=identity_operator.batch_shape,
    dtype=identity_operator.dtype,
    is_non_singular=True,
    is_self_adjoint=True,
    is_positive_definite=True,
    is_square=True))
