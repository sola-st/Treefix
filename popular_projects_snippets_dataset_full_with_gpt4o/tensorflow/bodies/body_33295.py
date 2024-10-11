# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_householder_test.py
shape = list(build_info.shape)
reflection_axis = linear_operator_test_util.random_sign_uniform(
    shape[:-1], minval=1., maxval=2., dtype=dtype)
# Make sure unit norm.
reflection_axis = reflection_axis / linalg_ops.norm(
    reflection_axis, axis=-1, keepdims=True)

lin_op_reflection_axis = reflection_axis

if use_placeholder:
    lin_op_reflection_axis = array_ops.placeholder_with_default(
        reflection_axis, shape=None)

operator = householder.LinearOperatorHouseholder(lin_op_reflection_axis)

mat = reflection_axis[..., array_ops.newaxis]
matrix = -2 * math_ops.matmul(mat, mat, adjoint_b=True)
matrix = array_ops.matrix_set_diag(
    matrix, 1. + array_ops.matrix_diag_part(matrix))

exit((operator, matrix))
