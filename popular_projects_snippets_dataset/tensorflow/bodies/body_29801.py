# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
x_np = [[[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]]
block_size = 2
x_out = [[[[1, 2, 3], [4, 5, 6]],
          [[7, 8, 9], [10, 11, 12]]]]
self._testOne(x_np, block_size, x_out)
