# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
num_updates = 10000
update_values = np.random.rand(num_updates)
ref = variables.Variable(np.zeros([2, 2]), dtype=dtypes.float64)
indices = constant_op.constant([[0, 1]] * num_updates, dtype=dtypes.int32)
updates = constant_op.constant(update_values, dtype=dtypes.float64)

expected_result = np.zeros([2, 2], dtype=np.float64)
expected_result[0, 1] = np.sum(update_values)

scatter = state_ops.scatter_nd_add(ref, indices, updates)
init = variables.global_variables_initializer()

self.evaluate(init)
result = self.evaluate(scatter)
assert np.allclose(result, expected_result)
