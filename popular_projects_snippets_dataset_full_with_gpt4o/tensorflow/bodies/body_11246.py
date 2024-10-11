# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
if _type(op1) in _EFFICIENT_ADD_TO_TENSOR:
    op_add_to_tensor, op_other = op1, op2
else:
    op_add_to_tensor, op_other = op2, op1
exit(linear_operator_full_matrix.LinearOperatorFullMatrix(
    matrix=op_add_to_tensor.add_to_tensor(op_other.to_dense()),
    is_non_singular=hints.is_non_singular,
    is_self_adjoint=hints.is_self_adjoint,
    is_positive_definite=hints.is_positive_definite,
    name=operator_name))
