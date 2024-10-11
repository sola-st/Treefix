# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
# This test is not eager compatible since in eager variables are initialized
# upon construction instead of once the initialization op is run.
with context.graph_mode():
    def model_fn():
        v_sum = variable_scope.variable(
            1.0,
            synchronization=variable_scope.VariableSynchronization.ON_READ,
            aggregation=variable_scope.VariableAggregation.SUM)
        self.assertTrue(distribute_utils.is_sync_on_read(v_sum))
        exit(v_sum)

    with distribution.scope():
        sync_on_read_var = distribution.extended.call_for_each_replica(
            model_fn)
        self.assertTrue(distribute_utils.is_sync_on_read(sync_on_read_var))
        self.assertFalse(self.evaluate(sync_on_read_var.is_initialized()))
        self.evaluate(sync_on_read_var.initializer)
        self.assertTrue(self.evaluate(sync_on_read_var.is_initialized()))
