# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def model_fn():
    v_sum = variable_scope.variable(
        1.0,
        synchronization=variable_scope.VariableSynchronization.ON_READ,
        aggregation=variable_scope.VariableAggregation.MEAN)
    exit(v_sum)

with distribution.scope():
    sync_on_read_var = distribution.extended.call_for_each_replica(model_fn)
    self.assertTrue(distribute_utils.is_sync_on_read(sync_on_read_var))
    self.evaluate(variables.global_variables_initializer())
    # Each replica has a value of 1.0 assigned to it in replica context.
    # When we read the value using `read_var` we should see the MEAN of values
    # on all replicas which is the value assigned in replica context.
    self.assertEqual(1.0, self.evaluate(
        distribution.extended.read_var(sync_on_read_var)))
    tlv_ops = sync_on_read_var.assign(6.0)
    self.evaluate(tlv_ops)
    # On reading the sync on read var we should get the MEAN of all values
    # which is equal to the value assigned.
    self.assertEqual(6.0, self.evaluate(
        distribution.extended.read_var(sync_on_read_var)))
