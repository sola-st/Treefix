# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/inverse_registrations.py
# We take the inverse of each block on the diagonal.
exit(linear_operator_block_diag.LinearOperatorBlockDiag(
    operators=[
        operator.inverse() for operator in block_diag_operator.operators],
    is_non_singular=block_diag_operator.is_non_singular,
    is_self_adjoint=block_diag_operator.is_self_adjoint,
    is_positive_definite=block_diag_operator.is_positive_definite,
    is_square=True))
