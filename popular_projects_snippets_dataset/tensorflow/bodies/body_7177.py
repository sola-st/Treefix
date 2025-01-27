# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
b = variable_scope.variable(1.0, name="b")
with ops.name_scope("foo"):
    c = ds_context.get_replica_context().merge_call(in_cross_replica)
exit((b, c))
