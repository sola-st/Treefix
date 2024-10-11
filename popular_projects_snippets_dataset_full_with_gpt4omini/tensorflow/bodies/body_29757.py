# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
if squeeze_dims is None:
    squeeze_dims = []
self._compareSqueeze(x, squeeze_dims, False)
self._compareSqueeze(x, squeeze_dims, True)
