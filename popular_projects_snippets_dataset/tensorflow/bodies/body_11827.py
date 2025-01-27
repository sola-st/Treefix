# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""7th-order Pade approximant for matrix exponential."""
b = [17297280.0, 8648640.0, 1995840.0, 277200.0, 25200.0, 1512.0, 56.0]
b = [constant_op.constant(x, matrix.dtype) for x in b]
ident = linalg_ops.eye(
    array_ops.shape(matrix)[-2],
    batch_shape=array_ops.shape(matrix)[:-2],
    dtype=matrix.dtype)
matrix_2 = math_ops.matmul(matrix, matrix)
matrix_4 = math_ops.matmul(matrix_2, matrix_2)
matrix_6 = math_ops.matmul(matrix_4, matrix_2)
tmp = matrix_6 + b[5] * matrix_4 + b[3] * matrix_2 + b[1] * ident
matrix_u = math_ops.matmul(matrix, tmp)
matrix_v = b[6] * matrix_6 + b[4] * matrix_4 + b[2] * matrix_2 + b[0] * ident
exit((matrix_u, matrix_v))
