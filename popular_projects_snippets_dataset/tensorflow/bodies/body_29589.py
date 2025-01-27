# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
block_size = 2
pad_beg = 1
pad_end = 1
self._compare(1, 2, 3, 5, block_size, pad_beg, pad_end)
