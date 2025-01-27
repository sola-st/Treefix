# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
if dtype == dtypes.bool:
    params = constant_op.constant([False, True, False, True])
    expected = constant_op.constant([[False, True], [False, True]])
else:
    params = constant_op.constant([6, 7, 8, 9], dtype=dtype)
    expected = constant_op.constant([[8, 7], [6, 9]], dtype=dtype)
indices = constant_op.constant([[2, 1], [0, 3]])
var = resource_variable_ops.ResourceVariable(params, name="var0")
with ops.control_dependencies([var.initializer]):
    result = resource_variable_ops.resource_gather(
        var.handle, indices, dtype=dtype)
self.assertAllEqual(expected, result)
