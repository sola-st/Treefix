# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variable_scope.variable(
        0.,
        synchronization=variables_lib.VariableSynchronization.ON_READ,
        aggregation=variables_lib.VariableAggregation.NONE)
self.evaluate(variables_lib.global_variables_initializer())
with self.assertRaisesRegex(
    ValueError, "Could not convert from .* VariableAggregation\\.NONE"):
    self.evaluate(v.read_value())
