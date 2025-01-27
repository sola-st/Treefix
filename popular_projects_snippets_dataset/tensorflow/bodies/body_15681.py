# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
x = ragged_factory_ops.constant(x)
y = ragged_factory_ops.constant(y)
wrapped_x = ragged_tensor.RaggedTensor.from_nested_row_splits(
    WrappedTensor(x.flat_values), x.nested_row_splits)
wrapped_y = ragged_tensor.RaggedTensor.from_nested_row_splits(
    WrappedTensor(y.flat_values), y.nested_row_splits)
res = op(x, y)
wrapped_res = op(wrapped_x, wrapped_y)
self.assertIsInstance(wrapped_res.flat_values, WrappedTensor)
self.assertAllEqual(wrapped_res.flat_values.value, res.flat_values)
self.assertAllTensorsEqual(wrapped_res.nested_row_splits,
                           res.nested_row_splits)
