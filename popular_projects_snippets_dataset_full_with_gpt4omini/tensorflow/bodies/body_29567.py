# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# The block size is 0.
x_np = [[[[1], [2]], [[3], [4]]]]
paddings = np.zeros((2, 2), dtype=np.int32)
block_size = 0
with self.assertRaises(ValueError):
    out_tf = self.space_to_batch(x_np, paddings, block_size)
    out_tf.eval()
