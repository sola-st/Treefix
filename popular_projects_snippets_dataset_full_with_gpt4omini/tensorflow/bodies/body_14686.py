# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
self._testBinOp([1, 2], [3, 4], [4, 6], lambda a, b: b.__radd__(a))
