# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, ValueError),
    'Last row partition does not match flat_values.'):
    sess = session.Session()
    with sess.as_default():
        rt = ragged_factory_ops.constant([[3], [4, 5], [6]])
        rt_shape = DynamicRaggedShape.from_tensor(rt)
        new_flat_values = constant_op.constant(['a', 'b', 'c'])
        rt2 = rt_shape._add_row_partitions(new_flat_values, validate=True)
        sess.run([rt2])
