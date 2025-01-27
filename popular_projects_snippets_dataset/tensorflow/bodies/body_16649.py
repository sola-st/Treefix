# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
v = resource_variable_ops.ResourceVariable([1.])
if not context.executing_eagerly():
    self.evaluate(v.initializer)

expected_handle_data = resource_variable_ops.get_eager_safe_handle_data(
    v.handle)

with ops.Graph().as_default():
    # Create a resource tensor without handle data. tf.placeholder could only
    # be called in graph mode.
    handle1 = array_ops.placeholder(dtypes.resource, [])
handle1_data = resource_variable_ops.get_eager_safe_handle_data(handle1)
self.assertFalse(handle1_data.is_set)

spec = resource_variable_ops.VariableSpec(shape=[1], dtype=dtypes.float32)
# Spec should set the handle shape and dtype of handle1.
handle2 = spec._from_components([handle1]).handle
handle2_data = resource_variable_ops.get_eager_safe_handle_data(handle2)
self.assertTrue(handle2_data.is_set)
self.assertEqual(handle2_data.shape_and_type[0].shape,
                 expected_handle_data.shape_and_type[0].shape)
self.assertEqual(handle2_data.shape_and_type[0].dtype,
                 expected_handle_data.shape_and_type[0].dtype)
