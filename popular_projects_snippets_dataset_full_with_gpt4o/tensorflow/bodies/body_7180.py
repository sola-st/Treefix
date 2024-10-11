# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
b = variable_scope.get_variable("b", [1])
with ops.name_scope("foo"):
    c = ds_context.get_replica_context().merge_call(in_cross_replica)
exit((b, c))
