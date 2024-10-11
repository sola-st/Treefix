# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
with context.eager_mode():
    x = constant_op.constant(np.ones((2, 2)).astype(np.float32))
    paddings = constant_op.constant([[1, 2], [3, 4]])
    constant_values = constant_op.constant(0.)
    gen_array_ops.pad_v2(x, paddings, constant_values)
    node_defs = self._get_new_node_defs()
    self.assertLen(node_defs, 1)
    (node_def,) = node_defs  # pylint: disable=unbalanced-tuple-unpacking
    self.assertEqual(node_def.op, 'PadV2')
    self.assertEqual(
        self._get_input_dtypes(node_def),
        [dtypes.float32, dtypes.int32, dtypes.float32])
    self.assertEqual(self._get_input_shapes(node_def), [(2, 2), (2, 2), ()])
    self.assertIsNone(self._get_input_tensor(node_def, 0))
    self.assertAllEqual(
        self._get_input_tensor(node_def, 1), np.array([[1, 2], [3, 4]]))
    self.assertIsNone(self._get_input_tensor(node_def, 2))
