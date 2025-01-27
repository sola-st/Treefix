# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
variable = variables.Variable(array_ops.ones([8], dtype=dtypes.int32))
resource_variable = resource_variable_ops.ResourceVariable(
    array_ops.ones([8], dtype=dtypes.int32))
indices = constant_op.constant([4, 3, 1, 7])
updates = constant_op.constant([0, 2, -1, 2], dtype=dtypes.int32)

for ref in (variable, resource_variable):
    sub_result = state_ops.scatter_sub(ref, indices, updates)
    self.evaluate(ref.initializer)

    expected_result = constant_op.constant([1, 2, 1, -1, 1, 1, 1, -1])
    self.assertAllEqual(self.evaluate(sub_result), expected_result)
    self.assertAllEqual(self.evaluate(ref), expected_result)
