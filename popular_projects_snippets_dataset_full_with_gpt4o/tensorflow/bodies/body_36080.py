# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(1.0, name="var0")
self.evaluate(variables.global_variables_initializer())
self.assertEqual(2.0, self.evaluate(v + v))
