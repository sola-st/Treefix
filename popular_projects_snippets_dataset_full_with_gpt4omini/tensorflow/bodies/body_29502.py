# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
x = np.arange(20 * 5 * 8 * 7, dtype=dtype).reshape([20, 5, 8, 7])
block_size = 2
for crops_dtype in [dtypes.int64, dtypes.int32]:
    crops = array_ops.zeros((2, 2), dtype=crops_dtype)
    y1 = self.batch_to_space(x, crops, block_size=block_size)
    y2 = array_ops.transpose(
        array_ops.depth_to_space(
            array_ops.transpose(x, [3, 1, 2, 0]), block_size=block_size),
        [3, 1, 2, 0])
    with self.cached_session():
        self.assertAllEqual(y1, y2)
