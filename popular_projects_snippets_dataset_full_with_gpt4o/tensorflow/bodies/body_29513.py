# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
# The block size is 0.
self._testShape([1, 2, 2, 1], [0, 1], [[0, 0], [0, 0]], ValueError)
