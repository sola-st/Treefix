# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = variables.Variable(1.0)
    self.assertIsInstance(v, resource_variable_ops.ResourceVariable)
