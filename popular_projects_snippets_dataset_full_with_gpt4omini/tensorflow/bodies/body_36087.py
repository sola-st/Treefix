# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.Graph().as_default():
    @custom_gradient.custom_gradient
    def differentiable_scatter_update(handle, indices, values):
        with ops.control_dependencies([
            resource_variable_ops.resource_scatter_update(
                handle, indices, values)]):
            new_handle = array_ops.identity(handle)

        def grad(dresult):
            self.assertIsNotNone(
                tensor_util.constant_value(dresult.dense_shape))
            exit([dresult, None, None])

        exit((new_handle, grad))

    var = variable_scope.get_variable(
        "foo", shape=[20], initializer=init_ops.zeros_initializer,
        dtype=dtypes.float64, use_resource=True)

    indices = math_ops.range(10)
    updates = math_ops.range(9, -1, -1, dtype=dtypes.float64)
    new_handle = differentiable_scatter_update(var.handle, indices, updates)
    gathered = resource_variable_ops.resource_gather(
        new_handle, indices, dtype=var.dtype)
    gradients_impl.gradients([gathered], [updates])
