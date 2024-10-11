# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variable_scope.variable(
        0.,
        synchronization=variables_lib.VariableSynchronization.ON_READ,
        aggregation=variables_lib.VariableAggregation.SUM)
self.evaluate(variables_lib.global_variables_initializer())
with self.assertRaisesRegex(
    ValueError, "SyncOnReadVariable does not support "):
    self.evaluate(v.assign_add(1.))
with self.assertRaisesRegex(
    ValueError, "SyncOnReadVariable does not support "):
    self.evaluate(v.assign_sub(1.))
