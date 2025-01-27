# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
old = variable_scope._DEFAULT_USE_RESOURCE
try:
    variable_scope.enable_resource_variables()
    self.assertTrue(isinstance(variables_lib.VariableV1(1.0),
                               resource_variable_ops.ResourceVariable))
    variable_scope.disable_resource_variables()
    self.assertFalse(isinstance(variables_lib.VariableV1(1.0),
                                resource_variable_ops.ResourceVariable))
finally:
    variable_scope._DEFAULT_USE_RESOURCE = old
