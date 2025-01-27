# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
if len(distribution.extended.parameter_devices) != 2:
    self.skipTest("n/a: needs exactly two parameter devices")
if (synchronization == variables_lib.VariableSynchronization.ON_WRITE and
    aggregation != variables_lib.VariableAggregation.NONE):
    self.skipTest("n/a: doesn't apply to ON_WRITE variable with aggregation")
with distribution.scope():
    v = variables_lib.Variable(
        0., synchronization=synchronization, aggregation=aggregation)
value = values_lib.PerReplica([1., 2.])

assign_fn = lambda var, value: var.assign(value)
self.evaluate(distribution.extended.update(v, assign_fn, args=(value,)))
self.assertAllEqual(self.evaluate(v.values), [1., 2.])

assign_add_fn = lambda var, value: var.assign_add(value)
self.evaluate(distribution.extended.update(v, assign_add_fn, args=(value,)))
self.assertAllEqual(self.evaluate(v.values), [2., 4.])

assign_sub_fn = lambda var, value: var.assign_sub(value)
self.evaluate(distribution.extended.update(v, assign_sub_fn, args=(value,)))
self.assertAllEqual(self.evaluate(v.values), [1., 2.])

read_assign_fn = lambda var, value: var.assign_add(var.value() + var.
                                                   read_value())
self.evaluate(
    distribution.extended.update(v, read_assign_fn, args=(value,)))
self.assertAllEqual(self.evaluate(v.values), [3., 6.])
