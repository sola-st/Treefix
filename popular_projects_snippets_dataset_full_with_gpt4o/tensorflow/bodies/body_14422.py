# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if x.dtype == dtypes.bool:
    exit(math_ops.logical_not(x))
exit(bitwise_ops.invert(x))
