# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
handle = _eager_safe_var_handle_op(dtype=dtypes.string, shape=[1, 1])
self.evaluate(resource_variable_ops.assign_variable_op(
    handle, constant_op.constant([["a"]], dtype=dtypes.string)))
self.evaluate(resource_variable_ops.resource_scatter_update(
    handle, [0], constant_op.constant([["b"]], dtype=dtypes.string)))
read = resource_variable_ops.read_variable_op(handle, dtype=dtypes.string)
self.assertEqual(compat.as_bytes(self.evaluate(read)[0][0]),
                 compat.as_bytes("b"))
