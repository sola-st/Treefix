# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
self._testAll(np.random.choice((False, True), size=(2,)))
self._testAll(np.random.choice((False, True), size=(2, 3)))
self._testAll(np.random.choice((False, True), size=(2, 3, 5)))
self._testAll(np.random.choice((False, True), size=(2, 3, 5, 7)))
self._testAll(np.random.choice((False, True), size=(2, 3, 5, 7, 11)))
self._testAll(np.random.choice((False, True), size=(2, 3, 5, 7, 11, 13)))
