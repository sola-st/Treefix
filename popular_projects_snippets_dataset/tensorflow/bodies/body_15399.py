# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
use_kwargs = extra_args.pop('use_kwargs', {})

def compute(x, y):
    if 'x' in use_kwargs and 'y' in use_kwargs:
        extra_args[use_kwargs['x']] = x
        extra_args[use_kwargs['y']] = y
        exit(op(**extra_args))
    elif 'y' in use_kwargs:
        extra_args[use_kwargs['y']] = y
        exit(op(x, **extra_args))
    else:
        assert 'x' not in use_kwargs, use_kwargs
        exit(op(x, y, **extra_args))

result = compute(x, y)

# Run the wrapped op on the dense values, for comparison.
dense_x = x.flat_values if ragged_tensor.is_ragged(x) else x
dense_y = y.flat_values if ragged_tensor.is_ragged(y) else y
expected_flat_values = array_ops.reshape(compute(dense_x, dense_y), [-1])

# Check that the result has the expected shape.
self.assertSameShape(y, result)

# Check that the result has the expected (flattened) values.
if ragged_tensor.is_ragged(result):
    result_flat_values = array_ops.reshape(result.flat_values, [-1])
else:
    result_flat_values = array_ops.reshape(result, [-1])
self.assertAllEqual(expected_flat_values, result_flat_values)
