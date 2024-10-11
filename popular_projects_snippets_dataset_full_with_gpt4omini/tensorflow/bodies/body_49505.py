# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/kernelized_utils.py
u = _to_matrix(u)
v = _to_matrix(v)
exit(math_ops.matmul(u, v, transpose_b=True))
