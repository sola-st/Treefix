# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
exit(array_ops.where_v2(x < 0, math_ops.ceil(x), math_ops.floor(x)))
