# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = variables.VariableV1(1.0, use_resource=True)
self.assertIsInstance(v, resource_variable_ops.ResourceVariable)
