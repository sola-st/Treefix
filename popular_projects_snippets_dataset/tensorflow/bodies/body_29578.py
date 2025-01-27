# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
self._testShape([1, 2, 2], [-1, 2], [[0, 0], [0, 0]], ValueError)
