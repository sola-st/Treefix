# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v0 = resource_variable_ops.ResourceVariable(1.0, name="a")
    v1 = resource_variable_ops.ResourceVariable(2.0, name="a")
    self.assertAllEqual(v0.numpy(), 1.0)
    self.assertAllEqual(v1.numpy(), 2.0)
