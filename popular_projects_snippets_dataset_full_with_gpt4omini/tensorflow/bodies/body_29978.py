# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
x = constant_op.constant([1]).shape[0]
self._testAll(x)
