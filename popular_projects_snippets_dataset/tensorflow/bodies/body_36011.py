# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session():
    handle = _eager_safe_var_handle_op(dtype=dtypes.int32, shape=[])
    with self.assertRaises(ValueError):
        resource_variable_ops.assign_variable_op(
            handle, constant_op.constant(0.0, dtype=dtypes.float32)).run()
    with self.assertRaises(ValueError):
        resource_variable_ops.assign_variable_op(handle,
                                                 constant_op.constant(
                                                     [0],
                                                     dtype=dtypes.int32)).run()
    resource_variable_ops.assign_variable_op(handle,
                                             constant_op.constant(
                                                 0,
                                                 dtype=dtypes.int32)).run()
