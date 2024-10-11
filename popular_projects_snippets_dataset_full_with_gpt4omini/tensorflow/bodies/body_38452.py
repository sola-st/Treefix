# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
if reduction_axes is not None and np.shape(reduction_axes) == (1,):
    # Test scalar reduction_axes argument
    self._compareAll(x, reduction_axes[0])
self._compare(x, reduction_axes, False, use_gpu=True, feed_dict=feed_dict)
self._compare(x, reduction_axes, False, use_gpu=False, feed_dict=feed_dict)
self._compare(x, reduction_axes, True, use_gpu=True, feed_dict=feed_dict)
self._compare(x, reduction_axes, True, use_gpu=False, feed_dict=feed_dict)
