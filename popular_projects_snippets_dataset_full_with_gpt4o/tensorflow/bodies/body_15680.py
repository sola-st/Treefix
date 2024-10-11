# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
x = ragged_factory_ops.constant(x, x_dtype)
wrapped_x = ragged_tensor.RaggedTensor.from_nested_row_splits(
    WrappedTensor(x.flat_values), x.nested_row_splits)
test_util.random_seed.set_seed(1234)
res = op(x, **extra_args)
test_util.random_seed.set_seed(1234)
wrapped_res = op(wrapped_x, **extra_args)
self.assertIsInstance(wrapped_res.flat_values, WrappedTensor)
self.assertAllEqual(wrapped_res.flat_values.value, res.flat_values)
self.assertAllTensorsEqual(wrapped_res.nested_row_splits,
                           res.nested_row_splits)
