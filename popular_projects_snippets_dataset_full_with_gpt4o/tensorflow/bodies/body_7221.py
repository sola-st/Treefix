# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
v_sum = variable_scope.variable(
    1.0,
    synchronization=variable_scope.VariableSynchronization.ON_READ,
    aggregation=variable_scope.VariableAggregation.SUM)
exit(v_sum)
