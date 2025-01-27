# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# The block size divides width but not height.
x_np = [[[[1], [2], [3]], [[3], [4], [7]]]]
paddings = np.zeros((2, 2), dtype=np.int32)
block_size = 3
with self.assertRaises(ValueError):
    _ = self.space_to_batch(x_np, paddings, block_size)
