# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
x_np = [[[[1, 10], [2, 20]], [[3, 30], [4, 40]]]]
block_size = 2
x_out = [[[[1, 10, 2, 20, 3, 30, 4, 40]]]]
self._testOne(x_np, block_size, x_out)
