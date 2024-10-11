# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# Shape of block_shape does not match shape of paddings.
self._testStaticShape([1, 3, 3, 1], [3, 3], [[0, 0]], ValueError)
