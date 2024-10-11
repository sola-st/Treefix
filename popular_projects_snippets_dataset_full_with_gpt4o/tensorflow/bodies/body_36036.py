# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
handle = _eager_safe_var_handle_op(dtype=dtypes.int32, shape=[])
self.evaluate(resource_variable_ops.assign_variable_op(
    handle, constant_op.constant(1, dtype=dtypes.int32)))
self.evaluate(resource_variable_ops.assign_add_variable_op(
    handle, constant_op.constant(1, dtype=dtypes.int32)))
read = self.evaluate(
    resource_variable_ops.read_variable_op(handle, dtype=dtypes.int32))
self.assertEqual(read, 2)
