# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
if reduction_axes is not None and np.shape(reduction_axes) == (1,):
    # Test scalar reduction_axes argument
    self._compareAll(x, reduction_axes[0], rtol=rtol, atol=atol)
self._compare(
    x,
    reduction_axes,
    keepdims=False,
    feed_dict=feed_dict,
    rtol=rtol,
    atol=atol)
self._compare(
    x,
    reduction_axes,
    keepdims=True,
    feed_dict=feed_dict,
    rtol=rtol,
    atol=atol)
