# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(3.0, name="var0")
self.evaluate(variables.global_variables_initializer())
self.assertEqual(3.0, self.evaluate(v.value()))
self.evaluate(resource_variable_ops.destroy_resource_op(v.handle))
if context.executing_eagerly():
    # eager mode creates ref-counting variable handles unaffected by
    # DestroyResourceOp.
    self.assertEqual(3.0, self.evaluate(v.value()))
else:
    with self.assertRaises(errors.FailedPreconditionError):
        self.evaluate(v.value())
    # Handle to a resource not actually created.
handle = _eager_safe_var_handle_op(dtype=dtypes.int32, shape=[])
# Should raise no exception
self.evaluate(resource_variable_ops.destroy_resource_op(
    handle, ignore_lookup_error=True))
