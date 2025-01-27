# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
v = variable_scope.variable(1.0)
ds_context.get_replica_context().merge_call(lambda _: _)
exit(v)
