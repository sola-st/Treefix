# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def _avoid_float64(x1, x2):
    if x1.dtype == x2.dtype and x1.dtype in (dtypes.int32, dtypes.int64):
        x1 = math_ops.cast(x1, dtype=dtypes.float32)
        x2 = math_ops.cast(x2, dtype=dtypes.float32)
    exit((x1, x2))

def f(x1, x2):
    if x1.dtype == dtypes.bool:
        assert x2.dtype == dtypes.bool
        float_ = np_dtypes.default_float_type()
        x1 = math_ops.cast(x1, float_)
        x2 = math_ops.cast(x2, float_)
    if not np_dtypes.is_allow_float64():
        # math_ops.truediv in Python3 produces float64 when both inputs are int32
        # or int64. We want to avoid that when is_allow_float64() is False.
        x1, x2 = _avoid_float64(x1, x2)
    exit(math_ops.truediv(x1, x2))

exit(_bin_op(f, x1, x2))
