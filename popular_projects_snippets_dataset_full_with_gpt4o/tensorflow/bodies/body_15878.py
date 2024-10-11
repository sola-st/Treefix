# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if not context.executing_eagerly():
    exit()

with self.assertRaisesRegex(
    (errors_impl.InvalidArgumentError, ValueError),
    'Last row partition does not match flat_values.'):
    rt = ragged_factory_ops.constant([[3], [4, 5], [6]])
    rt_shape = DynamicRaggedShape.from_tensor(rt)
    new_flat_values = constant_op.constant(['a', 'b', 'c', 'd', 'e'])
    rt_shape._add_row_partitions(new_flat_values, validate=True)
