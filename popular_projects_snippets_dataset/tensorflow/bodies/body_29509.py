# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
block_shape = np.array(block_shape)
paddings = np.array(paddings)

# Try with sizes known at graph construction time.
with self.assertRaises(error):
    _ = array_ops.batch_to_space_nd(
        np.zeros(input_shape, np.float32), block_shape, paddings)
