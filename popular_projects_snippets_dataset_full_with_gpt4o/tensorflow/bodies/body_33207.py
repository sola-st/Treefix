# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_adjoint_test.py
shape_before_adjoint = list(build_info.shape)
# We need to swap the last two dimensions because we are taking the adjoint
# of this operator
shape_before_adjoint[-1], shape_before_adjoint[-2] = (
    shape_before_adjoint[-2], shape_before_adjoint[-1])
matrix = linear_operator_test_util.random_normal(
    shape_before_adjoint, dtype=dtype)

lin_op_matrix = matrix

if use_placeholder:
    lin_op_matrix = array_ops.placeholder_with_default(matrix, shape=None)

operator = LinearOperatorAdjoint(
    linalg.LinearOperatorFullMatrix(lin_op_matrix))

exit((operator, linalg.adjoint(matrix)))
