# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
init_value = np.reshape(np.arange(np.power(4, 3)), (4, 4, 4))
v = resource_variable_ops.ResourceVariable(
    constant_op.constant(init_value, dtype=dtypes.int32), name="var3")
self.evaluate(variables.global_variables_initializer())

value = self.evaluate(v.sparse_read([0, 3, 1, 2]))
self.assertAllEqual(init_value[[0, 3, 1, 2], ...], value)
