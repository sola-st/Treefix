# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
tensor_values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
values = WrappedTensor(tensor_values)
nested_row_splits = [[0, 2, 5], [0, 2, 2, 5, 6, 7]]
rt = RaggedTensor.from_nested_row_splits(values, nested_row_splits)

tensor_int = constant_op.constant([1, 2, 3, 4, 5, 6, 7])
rt_int = rt.with_flat_values(tensor_int)
self.assertAllEqual(rt_int.flat_values, tensor_int)

rt_wrapped_int = rt.with_flat_values(WrappedTensor(tensor_int))
self.assertIsInstance(rt_wrapped_int.flat_values, WrappedTensor)
self.assertAllEqual(rt_wrapped_int.flat_values.value, tensor_int)
