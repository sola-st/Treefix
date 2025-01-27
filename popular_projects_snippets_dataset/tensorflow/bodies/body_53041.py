# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
# Ensure the converted graph has no variables and no function calls.
constant_graph_def = converted_concrete_func.graph.as_graph_def()
self.assertEqual(0, get_num_variables(constant_graph_def))
self.assertFalse(has_stateful_partitioned_call_op(constant_graph_def))

# Check that the converted ConcreteFunction produces the same result as the
# original Function.
expected_value = nest.flatten(func(**input_data))
actual_value = nest.flatten(converted_concrete_func(**input_data))

for expected, actual in zip(expected_value, actual_value):
    np.testing.assert_almost_equal(expected.numpy(), actual.numpy())

# Ensure the shape is retained.
for tensor in converted_concrete_func.inputs:
    actual_shape = input_data[tensor.name.split(":")[0]].shape
    self.assertEqual(tensor.shape, actual_shape)

# Save the converted ConcreteFunction as a signature.
save_dir = os.path.join(self.get_temp_dir(), "frozen_saved_model")
root = autotrackable.AutoTrackable()
root.f = converted_concrete_func
save(root, save_dir, {"mykey": converted_concrete_func})

# Load it back and make sure it works.
loaded_obj = load(save_dir)
actual_value = nest.flatten(loaded_obj.signatures["mykey"](**input_data))
for expected, actual in zip(expected_value, actual_value):
    np.testing.assert_almost_equal(expected.numpy(), actual.numpy())
