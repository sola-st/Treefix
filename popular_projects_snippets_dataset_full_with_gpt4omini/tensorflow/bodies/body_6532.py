# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
vs = []
vs.append(variable_scope.variable(1.0, name="foo/bar"))
vs.append(variable_scope.variable(1.0, name="foo_1/bar"))
vs.append(variable_scope.variable(1.0, name="foo_1/bar_1"))
vs.append(variable_scope.variable(1.0, name="foo/bar_1"))
ds_context.get_replica_context().merge_call(lambda _: _)
exit(vs)
