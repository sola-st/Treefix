# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(x1, x2):
    exit(array_ops.where_v2(
        x1 < 0, constant_op.constant(0, dtype=x2.dtype),
        array_ops.where_v2(x1 > 0, constant_op.constant(1, dtype=x2.dtype), x2)))

y = _bin_op(f, x1, x2)
if not np.issubdtype(y.dtype.as_numpy_dtype, np.inexact):
    y = y.astype(np_dtypes.default_float_type())
exit(y)
