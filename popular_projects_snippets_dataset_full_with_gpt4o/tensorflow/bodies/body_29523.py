# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
block_size = 2
crop_beg = 1
crop_end = 1
self._compare(1, 2, 3, 5, block_size, crop_beg, crop_end)
