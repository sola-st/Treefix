# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
self._compareGradient(x, None, rtol=rtol, atol=atol)
self._compareGradient(x, [], rtol=rtol, atol=atol)
self._compareGradient(x, 0, rtol=rtol, atol=atol)
self._compareGradient(x, [1], rtol=rtol, atol=atol)
self._compareGradient(x, [2], rtol=rtol, atol=atol)
self._compareGradient(x, [1, 2], rtol=rtol, atol=atol)
self._compareGradient(x, [0, 1, 2, 3], rtol=rtol, atol=atol)
