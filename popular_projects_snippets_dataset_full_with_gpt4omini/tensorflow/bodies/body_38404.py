# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
if isinstance(reduction_axes, list) or isinstance(reduction_axes,
                                                  np.ndarray):
    reduction_axes = tuple(reduction_axes)
exit(np.prod(x, axis=reduction_axes, keepdims=keepdims))
