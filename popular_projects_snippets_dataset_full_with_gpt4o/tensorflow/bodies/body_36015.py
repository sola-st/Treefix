# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v0 = resource_variable_ops.ResourceVariable(1.0)
    self.assertAllEqual(v0.numpy(), 1.0)
