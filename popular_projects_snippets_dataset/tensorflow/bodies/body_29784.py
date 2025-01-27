# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
self._RunAndVerifyGradientResult([2, 2, 1, 1, 3], [1, 1, 1, 1, 1])
self._RunAndVerifyGradientResult([2, 2, 1, 1, 3], [1, 2, 1, 3, 1])
self._RunAndVerifyGradientResult([2, 3, 1, 1, 3], [3, 1, 1, 2, 2])
self._RunAndVerifyGradientResult([2, 1, 3, 3, 2], [1, 3, 3, 1, 2])
