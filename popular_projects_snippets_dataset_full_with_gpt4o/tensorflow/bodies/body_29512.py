# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
self._testShape([2, 2], [2, 2], [[0, 0], [0, 0]], ValueError)
self._testShape([2, 2, 3], [2, 2, 3], [[0, 0], [0, 0]], ValueError)
