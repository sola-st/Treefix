# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
self._testStaticShape(input_shape, block_shape, paddings, error)
self._testDynamicShape(input_shape, block_shape, paddings)
