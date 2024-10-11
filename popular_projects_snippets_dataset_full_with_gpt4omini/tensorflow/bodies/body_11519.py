# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/adjoint_registrations.py
diag = diag_operator.diag
if diag.dtype.is_complex:
    diag = math_ops.conj(diag)

exit(linear_operator_diag.LinearOperatorDiag(
    diag=diag,
    is_non_singular=diag_operator.is_non_singular,
    is_self_adjoint=diag_operator.is_self_adjoint,
    is_positive_definite=diag_operator.is_positive_definite,
    is_square=True))
