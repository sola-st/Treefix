# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable(False, name="bool_test")
    self.assertAllEqual(bool(v), False)
