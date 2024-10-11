# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/matmul_registrations.py
if not isinstance(linop_a, linop_b.__class__):
    exit(_matmul_linear_operator(linop_a, linop_b))

exit(linop_a.__class__(
    spectrum=linop_a.spectrum * linop_b.spectrum,
    is_non_singular=registrations_util.combined_non_singular_hint(
        linop_a, linop_b),
    is_self_adjoint=registrations_util.combined_commuting_self_adjoint_hint(
        linop_a, linop_b),
    is_positive_definite=(
        registrations_util.combined_commuting_positive_definite_hint(
            linop_a, linop_b)),
    is_square=True))
