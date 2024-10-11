# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/matmul_registrations.py
"""Generic matmul of two `LinearOperator`s."""
is_square = registrations_util.is_square(linop_a, linop_b)
is_non_singular = None
is_self_adjoint = None
is_positive_definite = None

if is_square:
    is_non_singular = registrations_util.combined_non_singular_hint(
        linop_a, linop_b)
elif is_square is False:  # pylint:disable=g-bool-id-comparison
    is_non_singular = False
    is_self_adjoint = False
    is_positive_definite = False

exit(linear_operator_composition.LinearOperatorComposition(
    operators=[linop_a, linop_b],
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
))
