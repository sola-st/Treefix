# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
x_np = [[[[1], [2]], [[3], [4]]]]
block_size = 2
x_out = [[[[1]]], [[[2]]], [[[3]]], [[[4]]]]
self._testOne(x_np, block_size, x_out, dtype)
