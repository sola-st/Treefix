# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
ref = variables.Variable(array_ops.zeros([1]))
indices = array_ops.zeros([100000, 1], dtypes.int32)
values = np.random.randn(100000)
self.evaluate(variables.global_variables_initializer())
val = self.evaluate(state_ops.scatter_nd_update(ref, indices, values))
for _ in range(5):
    ref2 = variables.Variable(array_ops.zeros([1]))
    self.evaluate(variables.global_variables_initializer())
    val2 = self.evaluate(state_ops.scatter_nd_update(ref2, indices, values))
    self.assertAllEqual(val, val2)
