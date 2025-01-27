# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(
    np.random.uniform(size=[2, 2]), dtype=dtypes.float32)

with backprop.GradientTape() as tape:
    l = array_ops.gather_nd(v, [[1], [1]])
    l = math_ops.reduce_sum(l)

grads = tape.gradient(l, v)
self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(self.evaluate(grads.values), [[1., 1.], [1., 1.]])
