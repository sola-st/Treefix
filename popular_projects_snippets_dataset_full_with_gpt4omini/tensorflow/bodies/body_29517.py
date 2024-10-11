# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
# The batch dimension is not divisible by the product of the block_shape.
self._testShape([3, 1, 1, 1], [2, 3], [[0, 0], [0, 0]], ValueError)
