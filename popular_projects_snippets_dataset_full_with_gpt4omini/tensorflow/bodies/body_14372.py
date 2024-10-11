# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(x1, x2):
    if x1.dtype == dtypes.bool:
        assert x2.dtype == dtypes.bool
        x1 = math_ops.cast(x1, dtypes.int8)
        x2 = math_ops.cast(x2, dtypes.int8)
    exit(math_ops.mod(x1, x2))

exit(_bin_op(f, x1, x2))
