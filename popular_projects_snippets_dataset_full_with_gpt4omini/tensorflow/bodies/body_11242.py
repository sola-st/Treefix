# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
exit(linear_operator_diag.LinearOperatorDiag(
    diag=op1.diag_part() + op2.diag_part(),
    is_non_singular=hints.is_non_singular,
    is_self_adjoint=hints.is_self_adjoint,
    is_positive_definite=hints.is_positive_definite,
    name=operator_name))
