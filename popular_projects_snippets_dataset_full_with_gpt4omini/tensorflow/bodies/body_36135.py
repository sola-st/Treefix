# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
variant_shape_and_type_data = self.create_variant_shape_and_type_data()
value = self.create_constant_variant(3)
initializer = array_ops.fill([3], value)
resource_variable_ops._set_handle_shapes_and_types(  # pylint: disable=protected-access
    initializer, variant_shape_and_type_data,
    graph_mode=not context.executing_eagerly())
v = resource_variable_ops.ResourceVariable(initializer)
read = array_ops.identity(v)
read_variant_shape_and_type = (
    resource_variable_ops.get_eager_safe_handle_data(read))
self.assertEqual(
    read_variant_shape_and_type, variant_shape_and_type_data)
gather = v.sparse_read([0])
gather_variant_shape_and_type = (
    resource_variable_ops.get_eager_safe_handle_data(gather))
self.assertEqual(
    gather_variant_shape_and_type, variant_shape_and_type_data)
# Make sure initializer runs.
if not context.executing_eagerly():
    self.evaluate(v.initializer)
    self.evaluate(read.op)
    self.evaluate(gather.op)
