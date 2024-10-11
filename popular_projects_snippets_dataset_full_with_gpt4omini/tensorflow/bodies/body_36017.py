# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    variable = resource_variable_ops.ResourceVariable(1.0, name="eager-init")
    self.assertAllEqual(variable.numpy(), 1.0)
    self.assertAllEqual(variable.initialized_value().numpy(), 1.0)
