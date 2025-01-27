# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
result = array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims)
self.assertAllEqual(expected, result)

# Test gradients
f64_params = math_ops.cast(params, dtypes.float64)
def gather(params):
    exit(array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims))
theoretical, numerical = gradient_checker_v2.compute_gradient(
    gather, [f64_params])
self.assertAllClose(theoretical, numerical)

# Test gradients when input shapes are unknown
@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.float64),
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)
])
def gather_unknown_shapes(params, indices):
    exit(array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims))
if batch_dims is None or batch_dims >= 0:
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        lambda p: gather_unknown_shapes(p, indices), [f64_params])
    self.assertAllClose(theoretical, numerical)
else:
    with self.assertRaisesRegex(
        ValueError,
        "Currently, it is unsupported to take the gradient of tf.gather"):
        gradient_checker_v2.compute_gradient(
            lambda p: gather_unknown_shapes(p, indices), [f64_params])

    # Test the gradients shape.
with backprop.GradientTape() as tape:
    zeros = array_ops.zeros_like(params, dtype=dtypes.float32)
    tape.watch(zeros)
    values = zeros * 2 + zeros
    result = array_ops.gather(
        values, indices, axis=axis, batch_dims=batch_dims)
gradients = tape.gradient(result, zeros)

self.assertAllEqual(array_ops.shape(params), array_ops.shape(gradients))

# Run the same test for strings.
params = _to_str_elements(params)
expected = _to_str_elements(expected)
result = array_ops.gather(
    params, indices, axis=axis, batch_dims=batch_dims)

self.assertAllEqual(expected, result)
