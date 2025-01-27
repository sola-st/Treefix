# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
self._compareAll(x, None, rtol=rtol, atol=atol)
for axes in _powerset(range(x.ndim)):
    self._compareAll(x, axes, feed_dict, rtol=rtol, atol=atol)
