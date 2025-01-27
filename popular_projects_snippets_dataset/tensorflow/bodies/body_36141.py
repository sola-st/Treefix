# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = variables.Variable([1., 2.])
self.assertAllClose([1., 2.], list(iter(v)))
