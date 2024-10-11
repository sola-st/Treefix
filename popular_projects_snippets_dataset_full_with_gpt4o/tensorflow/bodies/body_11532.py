# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/matmul_registrations.py
exit(linear_operator_diag.LinearOperatorDiag(
    diag=linop_diag.diag * linop_scaled_identity.multiplier,
    is_non_singular=registrations_util.combined_non_singular_hint(
        linop_diag, linop_scaled_identity),
    is_self_adjoint=registrations_util.combined_commuting_self_adjoint_hint(
        linop_diag, linop_scaled_identity),
    is_positive_definite=(
        registrations_util.combined_commuting_positive_definite_hint(
            linop_diag, linop_scaled_identity)),
    is_square=True))
