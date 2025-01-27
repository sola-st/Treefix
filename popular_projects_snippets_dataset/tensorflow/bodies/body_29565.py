# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
x = np.arange(5 * 10 * 16 * 7, dtype=np.float32).reshape([5, 10, 16, 7])
block_size = 2
paddings = np.zeros((2, 2), dtype=np.int32)
y1 = self.space_to_batch(x, paddings, block_size=block_size)
y2 = array_ops.transpose(
    array_ops.space_to_depth(
        array_ops.transpose(x, [3, 1, 2, 0]), block_size=block_size),
    [3, 1, 2, 0])
with self.session():
    self.assertAllEqual(y1, y2)
