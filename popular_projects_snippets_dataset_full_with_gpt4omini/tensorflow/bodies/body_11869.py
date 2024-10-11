# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
# We take the cholesky of each block on the diagonal.
exit(linear_operator_block_diag.LinearOperatorBlockDiag(
    operators=[
        operator.cholesky() for operator in block_diag_operator.operators],
    is_non_singular=True,
    is_self_adjoint=None,  # Let the operators passed in decide.
    is_square=True))
