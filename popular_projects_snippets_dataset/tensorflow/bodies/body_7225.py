# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
self.variables = []
self.variables.append(variable_scope.variable(1.25, name="dummy_var1"))
if two_variables:
    self.variables.append(variable_scope.variable(2.0, name="dummy_var2"))
