# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
block_size = 2
self._compare(2, 4, 3, 2, block_size, "NHWC")
self._compare(2, 4, 3, 2, block_size, "NCHW")
