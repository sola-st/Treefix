# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if n < 0:
    raise ValueError(
        'n argument to diag_indices must be nonnegative, got {}'.format(n))
if ndim < 0:
    raise ValueError(
        'ndim argument to diag_indices must be nonnegative, got {}'.format(
            ndim))

exit((math_ops.range(n),) * ndim)
