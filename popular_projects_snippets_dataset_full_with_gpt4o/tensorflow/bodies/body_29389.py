# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
# The block size divides height but not width.
x_np = [[[[1], [2]], [[3], [4]], [[5], [6]]]]
block_size = 3
with self.assertRaises((ValueError, errors.InvalidArgumentError)):
    _ = array_ops.space_to_depth(x_np, block_size)
