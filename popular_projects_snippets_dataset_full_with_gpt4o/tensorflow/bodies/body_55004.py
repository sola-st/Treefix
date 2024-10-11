# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
with context.eager_mode():
    x32 = constant_op.constant(np.ones((2, 3)).astype(np.float32))
    y32 = constant_op.constant(np.ones((3, 2)).astype(np.float32))
    x64 = constant_op.constant(np.ones((2, 3)).astype(np.float64))
    y64 = constant_op.constant(np.ones((3, 2)).astype(np.float64))
    gen_math_ops.mat_mul(x32, y32)
    gen_math_ops.mat_mul(x64, y64)
    node_defs = self._get_new_node_defs()
    self.assertLen(node_defs, 2)
    node_def1, node_def2 = node_defs  # pylint: disable=unbalanced-tuple-unpacking
    if not IsMklEnabled():
        self.assertEqual(node_def1.op, 'MatMul')
    else:
        # Under certain conditions ops can be rewritten by oneDNN optimization
        # pass.
        self.assertIn(node_def1.op, ['MatMul', '_MklMatMul'])

    self.assertEqual(
        self._get_input_dtypes(node_def1), [dtypes.float32, dtypes.float32])
    self.assertEqual(self._get_input_shapes(node_def1), [(2, 3), (3, 2)])
    self.assertEqual(node_def2.op, 'MatMul')
    self.assertEqual(
        self._get_input_dtypes(node_def2), [dtypes.float64, dtypes.float64])
    self.assertEqual(self._get_input_shapes(node_def2), [(2, 3), (3, 2)])

    # The node is written again if the input shapes are different
    x32 = constant_op.constant(np.ones((4, 3)).astype(np.float32))
    gen_math_ops.mat_mul(x32, y32)
    node_defs = self._get_new_node_defs()
    self.assertLen(node_defs, 1)
    (node_def3,) = node_defs  # pylint: disable=unbalanced-tuple-unpacking
    if not IsMklEnabled():
        self.assertEqual(node_def3.op, 'MatMul')
    else:
        # Under certain conditions ops can be rewritten by oneDNN optimization
        # pass.
        self.assertIn(node_def3.op, ['MatMul', '_MklMatMul'])
    self.assertEqual(
        self._get_input_dtypes(node_def3), [dtypes.float32, dtypes.float32])
    self.assertEqual(self._get_input_shapes(node_def3), [(4, 3), (3, 2)])
