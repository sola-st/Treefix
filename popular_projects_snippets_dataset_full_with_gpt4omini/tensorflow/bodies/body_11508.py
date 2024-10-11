# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/solve_registrations.py
"""Solve of two ScaledIdentity `LinearOperators`."""
exit(linear_operator_identity.LinearOperatorScaledIdentity(
    num_rows=linop_a.domain_dimension_tensor(),
    multiplier=linop_b.multiplier / linop_a.multiplier,
    is_non_singular=registrations_util.combined_non_singular_hint(
        linop_a, linop_b),
    is_self_adjoint=registrations_util.combined_commuting_self_adjoint_hint(
        linop_a, linop_b),
    is_positive_definite=(
        registrations_util.combined_commuting_positive_definite_hint(
            linop_a, linop_b)),
    is_square=True))
