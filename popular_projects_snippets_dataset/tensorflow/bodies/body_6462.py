# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variable_scope.variable(
        0.,
        synchronization=variables_lib.VariableSynchronization.ON_READ,
        aggregation=variables_lib.VariableAggregation.SUM)
self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(v.assign(1. * distribution.num_replicas_in_sync))
for component in v._values:
    self.assertAllEqual(self.evaluate(component.read_value()),
                        self.evaluate(array_ops.ones_like(component)))
