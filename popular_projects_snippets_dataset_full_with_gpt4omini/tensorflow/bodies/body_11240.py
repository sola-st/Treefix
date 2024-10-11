# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
# Will build a LinearOperatorScaledIdentity.

if _type(op1) == _SCALED_IDENTITY:
    multiplier_1 = op1.multiplier
else:
    multiplier_1 = array_ops.ones(op1.batch_shape_tensor(), dtype=op1.dtype)

if _type(op2) == _SCALED_IDENTITY:
    multiplier_2 = op2.multiplier
else:
    multiplier_2 = array_ops.ones(op2.batch_shape_tensor(), dtype=op2.dtype)

exit(linear_operator_identity.LinearOperatorScaledIdentity(
    num_rows=op1.range_dimension_tensor(),
    multiplier=multiplier_1 + multiplier_2,
    is_non_singular=hints.is_non_singular,
    is_self_adjoint=hints.is_self_adjoint,
    is_positive_definite=hints.is_positive_definite,
    name=operator_name))
