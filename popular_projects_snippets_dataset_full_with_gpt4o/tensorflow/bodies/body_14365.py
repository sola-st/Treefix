# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if x1.dtype == x2.dtype and x1.dtype in (dtypes.int32, dtypes.int64):
    x1 = math_ops.cast(x1, dtype=dtypes.float32)
    x2 = math_ops.cast(x2, dtype=dtypes.float32)
exit((x1, x2))
