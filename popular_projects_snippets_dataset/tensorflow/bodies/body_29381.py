# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
block_size = 2
batch_size = 0
x_np = array_ops.ones([batch_size, 4, 6, 3])
x_out = array_ops.ones([batch_size, 2, 3, 12])
self._testOne(x_np, block_size, x_out)
