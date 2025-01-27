# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
v_sum = variable_scope.variable(
    1.0,
    synchronization=variable_scope.VariableSynchronization.ON_READ,
    aggregation=variable_scope.VariableAggregation.SUM)
self.assertTrue(distribute_utils.is_sync_on_read(v_sum))
exit(v_sum)
