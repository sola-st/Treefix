# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
x = ragged_tensor.convert_to_tensor_or_ragged_tensor(x)
random_seed.set_random_seed(1234)
result = op(x, **extra_args)

# Run the wrapped op on the dense values, for comparison.
dense_x = x.flat_values if ragged_tensor.is_ragged(x) else x
random_seed.set_random_seed(1234)
expected_flat_values = array_ops.reshape(op(dense_x, **extra_args), [-1])

# Check that the result has the expected shape.
self.assertSameShape(x, result)

# Check that the result has the expected (flattened) values.
if ragged_tensor.is_ragged(result):
    result_flat_values = array_ops.reshape(result.flat_values, [-1])
else:
    result_flat_values = array_ops.reshape(result, [-1])
self.assertAllEqual(expected_flat_values, result_flat_values)

if expected_dtype is not None:
    self.assertEqual(result.dtype, expected_dtype)
