# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
use_kwargs = extra_args.pop('use_kwargs', False)
if use_kwargs:
    result = op(inputs=inputs, **extra_args)
else:
    result = op(inputs, **extra_args)

# Run the wrapped op on the dense values, for comparison.
dense_inputs = [
    x.flat_values if ragged_tensor.is_ragged(x) else x for x in inputs
]
expected_flat_values = array_ops.reshape(
    op(dense_inputs, **extra_args), [-1])

# Check that the result has the expected shape.
self.assertSameShape(inputs[0], result)

# Check that the result has the expected (flattened) values.
if ragged_tensor.is_ragged(result):
    result_flat_values = array_ops.reshape(result.flat_values, [-1])
else:
    result_flat_values = array_ops.reshape(result, [-1])
self.assertAllEqual(expected_flat_values, result_flat_values)
