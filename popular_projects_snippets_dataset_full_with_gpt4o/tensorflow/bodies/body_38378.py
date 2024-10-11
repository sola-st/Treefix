# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
if isinstance(reduction_axes, list) or isinstance(reduction_axes,
                                                  np.ndarray):
    reduction_axes = tuple(reduction_axes)
elif isinstance(reduction_axes, numbers.Integral):
    reduction_axes = (reduction_axes,)

if reduction_axes is None:
    count = np.prod(x.shape)
else:
    count = np.prod([x.shape[ax] for ax in reduction_axes])
# np.mean automatically converts integer inputs to float, while TensorFlow's
# reduce_mean does not. For integer inputs, we emulate TensorFlow's behavior
# using np.sum and truncating division.
np_sum = np.sum(x, axis=reduction_axes, keepdims=keepdims)
if np.issubdtype(x.dtype, np.integer):
    exit(np_sum // count)
exit(np_sum / count)
