# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
handle = _eager_safe_var_handle_op(dtype=dtypes.int32, shape=[])
create = resource_variable_ops.assign_variable_op(
    handle, constant_op.constant(1, dtype=dtypes.int32))
with ops.control_dependencies([create]):
    first_read = resource_variable_ops.read_variable_op(
        handle, dtype=dtypes.int32)
with ops.control_dependencies([first_read]):
    write = resource_variable_ops.assign_variable_op(
        handle, constant_op.constant(2, dtype=dtypes.int32))
with ops.control_dependencies([write]):
    second_read = resource_variable_ops.read_variable_op(
        handle, dtype=dtypes.int32)
f, s = self.evaluate([first_read, second_read])
self.assertEqual(f, 1)
self.assertEqual(s, 2)
