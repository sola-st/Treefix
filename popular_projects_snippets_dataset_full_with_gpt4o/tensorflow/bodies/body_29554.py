# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
x_np = [[[[1], [2], [3], [4]], [[5], [6], [7], [8]],
         [[9], [10], [11], [12]], [[13], [14], [15], [16]]]]
block_size = 2
x_out = [[[[1], [3]], [[9], [11]]], [[[2], [4]], [[10], [12]]],
         [[[5], [7]], [[13], [15]]], [[[6], [8]], [[14], [16]]]]
self._testOne(x_np, block_size, x_out)
