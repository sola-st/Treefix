# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""3rd-order Pade approximant for matrix exponential."""
b = [120.0, 60.0, 12.0]
b = [constant_op.constant(x, matrix.dtype) for x in b]
ident = linalg_ops.eye(
    array_ops.shape(matrix)[-2],
    batch_shape=array_ops.shape(matrix)[:-2],
    dtype=matrix.dtype)
matrix_2 = math_ops.matmul(matrix, matrix)
tmp = matrix_2 + b[1] * ident
matrix_u = math_ops.matmul(matrix, tmp)
matrix_v = b[2] * matrix_2 + b[0] * ident
exit((matrix_u, matrix_v))
