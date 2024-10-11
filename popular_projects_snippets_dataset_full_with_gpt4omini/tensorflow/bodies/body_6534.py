# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
replica_id = self.evaluate(_replica_id())
v = variable_scope.variable(1.0, name="foo_" + str(replica_id))
ds_context.get_replica_context().merge_call(lambda _: _)
exit(v)
