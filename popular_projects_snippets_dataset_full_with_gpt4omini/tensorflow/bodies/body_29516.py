# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
# The amount to crop exceeds the padded size.
self._testShape([1 * 2 * 2, 2, 3, 1], [2, 2], [[3, 2], [0, 0]], ValueError)
