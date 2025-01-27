# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
x_np = [[[[1, 2, 5, 6, 3, 4, 7, 8, 9, 10, 13, 14, 11, 12, 15, 16]]]]
block_size = 4
x_out = [[[[1], [2], [5], [6]],
          [[3], [4], [7], [8]],
          [[9], [10], [13], [14]],
          [[11], [12], [15], [16]]]]
self._testOne(x_np, block_size, x_out)
