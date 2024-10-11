# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
# The block size squared does not divide the batch.
x_np = [[[[1], [2], [3]], [[3], [4], [7]]]]
crops = np.zeros((2, 2), dtype=np.int32)
block_size = 3
with self.assertRaises(ValueError):
    _ = self.batch_to_space(x_np, crops, block_size)
