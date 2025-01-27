# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
v0 = variable_scope.variable(1.0, name="var0", aggregation=None)
with variable_scope.variable_scope("common"):
    v1 = variable_scope.variable(1.0, name="var1")
    # This will pause the current thread, and execute the other thread.
    ds_context.get_replica_context().merge_call(lambda _: _)
    v2 = variable_scope.variable(
        1.0,
        name="var2",
        synchronization=variable_scope.VariableSynchronization.ON_READ,
        aggregation=variable_scope.VariableAggregation.SUM)
    v3 = variable_scope.variable(
        1.0,
        name="var3",
        synchronization=variable_scope.VariableSynchronization.ON_WRITE,
        aggregation=variable_scope.VariableAggregation.MEAN)

exit((v0, v1, v2, v3))
