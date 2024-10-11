# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
handle = _eager_safe_var_handle_op(dtype=dtypes.int32, shape=[])
id_handle = array_ops.identity(handle)
self.evaluate(resource_variable_ops.assign_variable_op(
    id_handle, constant_op.constant(0, dtype=dtypes.int32)))
