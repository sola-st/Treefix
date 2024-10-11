# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
"""Checks that batch_dims matches multiple calls to tf.gather()."""
# Generate a `params` tensor with the indicated shape.
params_size = np.prod(params_shape)
params = np.reshape(np.arange(params_size), params_shape)

# Generate an `indices` tensor with the indicated shape, where each index
# is within the appropriate range.
indices_size = np.prod(indices_shape)
indices = np.reshape(np.arange(indices_size), indices_shape)
indices = indices % params_shape[axis]

# Perform repeated (batched) gather operations with numpy, to find the
# expected result.
expected = self._batchNumpyGather(params, indices, axis, batch_dims)

# On Windows, we get an exception if we pass in the transformed numpy
# arrays ("Failed to convert numpy ndarray to a Tensor (Unsupported
# feed type)."); so convert them back to lists before calling tf.gather.
params = params.tolist()
indices = indices.tolist()

result = array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims)
self.assertAllEqual(output_shape, result.shape.as_list())
self.assertAllEqual(expected, result)

# Run the same test for strings.
params = _to_str_elements(params)
expected = _to_str_elements(expected.tolist())
result = array_ops.gather(
    params, indices, axis=axis, batch_dims=batch_dims)

self.assertAllEqual(output_shape, result.shape.as_list())
self.assertAllEqual(expected, result)
