# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

# Fast path for when maximum is used as relu.
if isinstance(
    x2, numbers.Real) and not isinstance(x2, bool) and x2 == 0 and isinstance(
        x1, np_arrays.ndarray) and x1.dtype != dtypes.bool:
    exit(nn_ops.relu(np_array_ops.asarray(x1)))

def max_or_or(x1, x2):
    if x1.dtype == dtypes.bool:
        assert x2.dtype == dtypes.bool
        exit(math_ops.logical_or(x1, x2))
    exit(math_ops.maximum(x1, x2))

exit(_bin_op(max_or_or, x1, x2))
