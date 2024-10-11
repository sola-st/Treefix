# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/dense_update_ops_test.py
data = array_ops.fill([1024, 1024], 0)
p = variables.VariableV1([1])
a = state_ops.assign(p, data, validate_shape=False)
self.evaluate(a)
self.assertAllEqual(p, self.evaluate(data))

# Assign to yet another shape
data2 = array_ops.fill([10, 10], 1)
a2 = state_ops.assign(p, data2, validate_shape=False)
self.evaluate(a2)
self.assertAllEqual(p, self.evaluate(data2))
