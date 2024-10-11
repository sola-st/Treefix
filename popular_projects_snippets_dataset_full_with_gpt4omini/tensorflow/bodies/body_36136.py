# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
var = resource_variable_ops.ResourceVariable(params, name="var0")
with ops.control_dependencies([var.initializer]):
    result = resource_variable_ops.resource_gather(
        var.handle, indices, dtype=var.dtype, batch_dims=batch_dims)
self.assertAllEqual(expected, result)
