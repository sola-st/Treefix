# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
aggregation = variable_scope.VariableAggregation.ONLY_FIRST_REPLICA
v0 = variable_scope.variable(
    2.0,
    name="on_read",
    synchronization=variable_scope.VariableSynchronization.ON_READ,
    aggregation=aggregation)
v1 = variable_scope.variable(
    3.0,
    name="on_write",
    synchronization=variable_scope.VariableSynchronization.ON_WRITE,
    aggregation=aggregation)
exit((v0, v1))
