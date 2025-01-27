# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
self._testCmp([1, 2, 3], [3, 2, 1], [True, False, False],
              lambda a, b: a.__lt__(b))
