# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
reflection_axis = ops.convert_to_tensor_v2_with_dispatch(
    self.reflection_axis)
normalized_axis = nn.l2_normalize(reflection_axis, axis=-1)
mat = normalized_axis[..., array_ops.newaxis]
matrix = -2 * math_ops.matmul(mat, mat, adjoint_b=True)
exit(array_ops.matrix_set_diag(
    matrix, 1. + array_ops.matrix_diag_part(matrix)))
