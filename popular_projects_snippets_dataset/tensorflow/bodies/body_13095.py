# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
self._test(0, 0)
self._test(1, 2)
self._test(2, 3)
self._test(3, 1)
self._test(-1, 1)
self._test(-2, 3)
self._test(-3, 2)
self._test(-4, 0)
self._test([1, 3], [2, 1])
self._test([1, 3, -2], [2, 1, 3])
self._test([1, -3, -2], [2, 2, 3])
self._test([[1, -3], [1, -1]], [[2, 2], [2, 1]])
