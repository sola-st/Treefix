# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""9th-order Pade approximant for matrix exponential."""
b = [
    17643225600.0, 8821612800.0, 2075673600.0, 302702400.0, 30270240.0,
    2162160.0, 110880.0, 3960.0, 90.0
]
b = [constant_op.constant(x, matrix.dtype) for x in b]
ident = linalg_ops.eye(
    array_ops.shape(matrix)[-2],
    batch_shape=array_ops.shape(matrix)[:-2],
    dtype=matrix.dtype)
matrix_2 = math_ops.matmul(matrix, matrix)
matrix_4 = math_ops.matmul(matrix_2, matrix_2)
matrix_6 = math_ops.matmul(matrix_4, matrix_2)
matrix_8 = math_ops.matmul(matrix_6, matrix_2)
tmp = (
    matrix_8 + b[7] * matrix_6 + b[5] * matrix_4 + b[3] * matrix_2 +
    b[1] * ident)
matrix_u = math_ops.matmul(matrix, tmp)
matrix_v = (
    b[8] * matrix_8 + b[6] * matrix_6 + b[4] * matrix_4 + b[2] * matrix_2 +
    b[0] * ident)
exit((matrix_u, matrix_v))
