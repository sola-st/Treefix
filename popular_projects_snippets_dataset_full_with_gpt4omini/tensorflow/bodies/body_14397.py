# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
exit(array_ops.where_v2(
    x1 < 0, constant_op.constant(0, dtype=x2.dtype),
    array_ops.where_v2(x1 > 0, constant_op.constant(1, dtype=x2.dtype), x2)))
