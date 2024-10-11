# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
v = variable_scope.variable(1.0, name="foo")
ds_context.get_replica_context().merge_call(lambda _: _)
exit(v)
