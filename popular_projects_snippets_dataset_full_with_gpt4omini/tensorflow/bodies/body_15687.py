# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
wrapped_tensor = WrappedTensor(constant_op.constant(flat_values))
rt = RaggedTensor.from_nested_row_splits(wrapped_tensor, nested_row_splits)
components = rt_spec._to_components(rt)
self.assertIsInstance(components[0], WrappedTensor)
self.assertAllEqual(components[0].value, wrapped_tensor.value)
self.assertAllTensorsEqual(components[1:], nested_row_splits)
rt_reconstructed = rt_spec._from_components(components)
self.assertIsInstance(rt_reconstructed.flat_values, WrappedTensor)
self.assertAllEqual(rt_reconstructed.flat_values.value,
                    wrapped_tensor.value)
self.assertAllTensorsEqual(rt_reconstructed.nested_row_splits,
                           rt.nested_row_splits)
self.assertEqual(rt_reconstructed.dtype, rt.dtype)
