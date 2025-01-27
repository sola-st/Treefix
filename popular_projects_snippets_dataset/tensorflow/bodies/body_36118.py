# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    var = resource_variable_ops.ResourceVariable(initial_value=1.0,
                                                 name="var8")
    var_handle = test_ops.make_weak_resource_handle(var._handle)
    del var
    with self.assertRaisesRegex(errors.NotFoundError,
                                r"Resource .* does not exist."):
        resource_variable_ops.destroy_resource_op(var_handle,
                                                  ignore_lookup_error=False)
