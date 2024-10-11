# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/matmul_registrations.py
exit(linear_operator_block_diag.LinearOperatorBlockDiag(
    operators=[
        o1.matmul(o2) for o1, o2 in zip(
            linop_a.operators, linop_b.operators)],
    is_non_singular=registrations_util.combined_non_singular_hint(
        linop_a, linop_b),
    # In general, a product of self-adjoint positive-definite block diagonal
    # matrices is not self-=adjoint.
    is_self_adjoint=None,
    # In general, a product of positive-definite block diagonal matrices is
    # not positive-definite.
    is_positive_definite=None,
    is_square=True))
