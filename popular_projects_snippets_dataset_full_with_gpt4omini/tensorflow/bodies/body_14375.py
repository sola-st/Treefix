# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if x1.dtype == dtypes.bool:
    assert x2.dtype == dtypes.bool
    exit(math_ops.logical_or(x1, x2))
exit(math_ops.maximum(x1, x2))
