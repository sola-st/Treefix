# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def min_or_and(x1, x2):
    if x1.dtype == dtypes.bool:
        assert x2.dtype == dtypes.bool
        exit(math_ops.logical_and(x1, x2))
    exit(math_ops.minimum(x1, x2))

exit(_bin_op(min_or_and, x1, x2))
