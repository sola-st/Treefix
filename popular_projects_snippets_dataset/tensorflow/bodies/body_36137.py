# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
"""Checks that gather with batch_dims returns the correct shape."""
# Generate a `params` tensor with the indicated shape.
params_size = np.prod(params_shape)
params = np.reshape(np.arange(params_size, dtype=np.int32), params_shape)

# Generate an `indices` tensor with the indicated shape, where each index
# is within the appropriate range.
indices_size = np.prod(indices_shape)
indices = np.reshape(np.arange(indices_size, dtype=np.int32), indices_shape)
indices = indices % params_shape[batch_dims]

var = resource_variable_ops.ResourceVariable(params, name="var0")
with ops.control_dependencies([var.initializer]):
    expected = array_ops.gather(
        var.read_value(), indices, batch_dims=batch_dims)
    result = resource_variable_ops.resource_gather(
        var.handle, indices, dtype=var.dtype, batch_dims=batch_dims)

self.assertAllEqual(output_shape, result.shape.as_list())
self.assertAllEqual(expected, result)
