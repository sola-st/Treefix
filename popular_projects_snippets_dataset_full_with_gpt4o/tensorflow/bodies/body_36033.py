# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(1.0)
self.assertNotEqual(v.name, v.assign_add(1.0).name)
