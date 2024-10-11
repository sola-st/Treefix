# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
init_value = np.reshape(np.arange(np.power(4, 3)), (4, 4, 4))
v = resource_variable_ops.ResourceVariable(
    constant_op.constant(init_value, dtype=dtypes.int32), name="var3")
self.evaluate(variables.global_variables_initializer())

value_op = v.gather_nd([[0, 0], [1, 2], [3, 3]])
self.assertAllEqual([3, 4], value_op.shape)
value = self.evaluate(value_op)
self.assertAllEqual([[0, 1, 2, 3], [24, 25, 26, 27], [60, 61, 62, 63]],
                    value)

value_op = v.gather_nd([[0, 0, 0], [1, 2, 3], [3, 3, 3]])
self.assertAllEqual([3], value_op.shape)
value = self.evaluate(value_op)
self.assertAllEqual([0, 27, 63], value)
