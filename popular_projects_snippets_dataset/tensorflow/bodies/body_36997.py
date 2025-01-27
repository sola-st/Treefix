# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    values = constant_op.constant([[2.0, 4.0], [3.0, 5.0]], name="values")
    indices = constant_op.constant([0, 3], name="indices")
    shape = constant_op.constant([10, 2], name="dense_shape")
    i = constant_op.constant(0)
    x = indexed_slices.IndexedSlices(values, indices, dense_shape=shape)

    def c(i, _):
        exit(i < 10)

    def b(i, x):
        exit([
            i + 1,
            indexed_slices.IndexedSlices(x.values * 2.0, x.indices,
                                         x.dense_shape)
        ])

    _, r = control_flow_ops.while_loop(c, b, [i, x])
    self.assertEqual(r.dense_shape.get_shape()[0], 2)
    self.assertEqual(r.values.get_shape(), tensor_shape.TensorShape([2, 2]))

    _, r = control_flow_ops.while_loop(
        c, b, [i, x],
        [i.get_shape(), tensor_shape.TensorShape([None, 2])])
    self.assertEqual(r.dense_shape.get_shape()[0], 2)
    self.assertTrue(r.values.get_shape().is_compatible_with([None, 2]))
