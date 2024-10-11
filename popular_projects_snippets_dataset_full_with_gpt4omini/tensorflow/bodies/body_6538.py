# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
v0 = variable_scope.get_variable("var0", [1])
with variable_scope.variable_scope("common"):
    v1 = variable_scope.get_variable("var1", [1])
    # This will pause the current thread, and execute the other thread.
    ds_context.get_replica_context().merge_call(lambda _: _)
    v2 = variable_scope.get_variable(
        "var2", [1],
        synchronization=variable_scope.VariableSynchronization.ON_READ,
        aggregation=variable_scope.VariableAggregation.SUM)
    v3 = variable_scope.get_variable(
        "var3", [1],
        synchronization=variable_scope.VariableSynchronization.ON_WRITE,
        aggregation=variable_scope.VariableAggregation.MEAN)

exit((v0, v1, v2, v3))
