# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
is_bool = (x1.dtype == dtypes.bool)
if is_bool:
    assert x2.dtype == dtypes.bool
    x1 = math_ops.cast(x1, dtypes.int8)
    x2 = math_ops.cast(x2, dtypes.int8)
r = tf_fn(x1, x2)
if is_bool:
    r = math_ops.cast(r, dtypes.bool)
exit(r)
