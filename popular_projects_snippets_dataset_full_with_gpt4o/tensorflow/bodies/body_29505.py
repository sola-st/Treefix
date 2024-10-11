# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
# The block size is 1. The block size needs to be > 1.
x_np = [[[[1], [2]], [[3], [4]]]]
crops = np.zeros((2, 2), dtype=np.int32)
block_size = 1
with self.assertRaises(ValueError):
    out_tf = self.batch_to_space(x_np, crops, block_size)
    out_tf.eval()
