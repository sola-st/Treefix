# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
block_size = 2
self._compare(3, 2, 5, 3, block_size, "NHWC")
self._compare(3, 2, 5, 3, block_size, "NCHW")
