# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.device('/cpu:0'):
    v0_0 = resource_variable_ops.ResourceVariable(1.0)
with ops.device('/cpu:1'):
    v0_1 = resource_variable_ops.ResourceVariable(2.0)
    v1_0 = resource_variable_ops.ResourceVariable(3.0)
with ops.device('/cpu:2'):
    v1_1 = resource_variable_ops.ResourceVariable(4.0)

packed_var_0 = ops.pack_eager_tensors([v0_0.handle, v0_1.handle])
packed_var_1 = ops.pack_eager_tensors([v1_0.handle, v1_1.handle])

# TODO(b/145922293): use ResourceVariable.assign_add and
# ResourceVariable.read_value directly once we support packing multiple
# ResourceVariable into one ResourceVariable.
@polymorphic_function.function
def read_var():
    resource_variable_ops.assign_add_variable_op(packed_var_0,
                                                 constant_op.constant(5.0))
    resource_variable_ops.assign_add_variable_op(packed_var_1,
                                                 constant_op.constant(6.0))
    with ops.device('/cpu:0'):
        read0 = resource_variable_ops.read_variable_op(
            packed_var_0, dtype=dtypes.float32)
    with ops.device('/cpu:1'):
        read1 = resource_variable_ops.read_variable_op(
            packed_var_0, dtype=dtypes.float32)
        read2 = resource_variable_ops.read_variable_op(
            packed_var_1, dtype=dtypes.float32)
    with ops.device('/cpu:2'):
        read3 = resource_variable_ops.read_variable_op(
            packed_var_1, dtype=dtypes.float32)

    exit((read0, read1, read2, read3))

arg_attrs = read_var.get_concrete_function().function_def.arg_attr
self.assertLen(arg_attrs, 2)
self.assertEqual(arg_attrs[0].attr['_composite_device'].s,
                 compat.as_bytes(packed_var_0.device))
self.assertEqual(arg_attrs[1].attr['_composite_device'].s,
                 compat.as_bytes(packed_var_1.device))

self.assertAllEqual(read_var(), (1 + 5, 2 + 5, 3 + 6, 4 + 6))
