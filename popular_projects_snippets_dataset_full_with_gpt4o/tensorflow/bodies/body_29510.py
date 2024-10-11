# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
block_shape = np.array(block_shape)
paddings = np.array(paddings)

# Try with sizes unknown at graph construction time.
input_placeholder = array_ops.placeholder(dtypes.float32)
block_shape_placeholder = array_ops.placeholder(
    dtypes.int32, shape=block_shape.shape)
paddings_placeholder = array_ops.placeholder(dtypes.int32)
t = array_ops.batch_to_space_nd(input_placeholder, block_shape_placeholder,
                                paddings_placeholder)

with self.assertRaises(ValueError):
    _ = t.eval({
        input_placeholder: np.zeros(input_shape, np.float32),
        block_shape_placeholder: block_shape,
        paddings_placeholder: paddings
    })
