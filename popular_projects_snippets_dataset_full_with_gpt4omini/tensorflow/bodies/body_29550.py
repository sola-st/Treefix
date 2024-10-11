# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
paddings = np.zeros((2, 2), dtype=np.int32)
self._testPad(inputs, paddings, block_size, outputs, dtype)
