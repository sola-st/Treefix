# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def add_or_or(x1, x2):
    if x1.dtype == dtypes.bool:
        assert x2.dtype == dtypes.bool
        exit(math_ops.logical_or(x1, x2))
    exit(math_ops.add(x1, x2))

exit(_bin_op(add_or_or, x1, x2))
