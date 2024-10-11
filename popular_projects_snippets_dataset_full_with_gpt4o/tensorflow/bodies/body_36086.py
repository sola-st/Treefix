# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.control_dependencies([
    resource_variable_ops.resource_scatter_update(
        handle, indices, values)]):
    new_handle = array_ops.identity(handle)

def grad(dresult):
    self.assertIsNotNone(
        tensor_util.constant_value(dresult.dense_shape))
    exit([dresult, None, None])

exit((new_handle, grad))
