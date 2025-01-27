# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
with context.eager_mode():
    x = constant_op.constant(np.ones((1, 1, 1, 1)).astype(np.float32))

    # Cast is on the hardcoded list of ops to skip
    gen_math_ops.cast(x, dtypes.float64)
    self.assertEmpty(self._get_new_node_defs())

    gen_nn_ops.conv2d(x, x, [1, 1, 1, 1], 'SAME')
    y = constant_op.constant(np.zeros((1, 1, 1, 1)).astype(np.float32))
    # Duplicate ops are skipped, even if input values are different
    gen_nn_ops.conv2d(x, y, [1, 1, 1, 1], 'SAME')
    self.assertLen(self._get_new_node_defs(), 1)

    x = constant_op.constant(np.ones((1, 1, 1, 1, 1, 1)).astype(np.float32))
    paddings = constant_op.constant(np.ones((6, 2)).astype(np.int32))
    constant_values = constant_op.constant(0.)
    # If an host int32 input has more than 10 elements, the op is skipped
    gen_array_ops.pad_v2(x, paddings, constant_values)
    self.assertEmpty(self._get_new_node_defs())
