# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/matmul_registrations.py
exit(linear_operator_diag.LinearOperatorDiag(
    diag=linop_a.diag * linop_b.diag,
    is_non_singular=registrations_util.combined_non_singular_hint(
        linop_a, linop_b),
    is_self_adjoint=registrations_util.combined_commuting_self_adjoint_hint(
        linop_a, linop_b),
    is_positive_definite=(
        registrations_util.combined_commuting_positive_definite_hint(
            linop_a, linop_b)),
    is_square=True))
