# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    v_sum = variable_scope.variable(
        1.0,
        synchronization=variable_scope.VariableSynchronization.ON_READ,
        aggregation=variable_scope.VariableAggregation.SUM)
    self.assertTrue(distribute_utils.is_sync_on_read(v_sum))
    exit(v_sum)

def update(var, value):
    exit(var.assign(value))

with distribution.scope():
    ret_v_sum = distribution.extended.call_for_each_replica(model_fn)

    # Initialize variables.
    self.evaluate(variables.global_variables_initializer())
    # Assert that the aggregated value of the sync on read var is the sum
    # of the individual values before running the update ops.
    self.assertEqual(
        1.0,
        self.evaluate(
            distribution.experimental_local_results(ret_v_sum)
            [0].read_value()))
    self.assertEqual(2.0, self.evaluate(ret_v_sum))

    # Apply updates.
    update_ops = distribution.extended.update(
        ret_v_sum, update, args=(5.0,), group=False)
    self.evaluate(update_ops)
    # Assert that the aggregated value of the sync on read vars is the sum
    # of the individual values after running the update ops.
    self.assertEqual(
        5.0,
        self.evaluate(
            distribution.experimental_local_results(ret_v_sum)
            [0].read_value()))
    self.assertEqual(10.0, self.evaluate(ret_v_sum))
