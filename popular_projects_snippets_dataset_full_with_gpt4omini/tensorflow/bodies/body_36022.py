# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([1.0, 2.0])
self.evaluate(variables.global_variables_initializer())
self.evaluate(v[0].assign(2.0))
self.assertAllEqual(self.evaluate(v), [2.0, 2.0])
