# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
exit(np_utils.cond(
    math_ops.equal(array_ops.size(v), 0),
    lambda: array_ops.zeros([abs(k), abs(k)], dtype=v.dtype),
    lambda: array_ops.matrix_diag(v, k=k)))
