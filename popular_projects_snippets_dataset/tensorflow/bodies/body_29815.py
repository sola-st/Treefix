# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
block_size = 3
self._compare(1, 2, 3, 2, block_size, "NHWC")
self._compare(1, 2, 3, 2, block_size, "NCHW")
