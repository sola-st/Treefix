# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# The padded size is not divisible by the block size.
self._testShape([1, 2, 3, 1], [3, 3], [[0, 0], [0, 0]], ValueError)
