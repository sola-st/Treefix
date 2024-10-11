# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
vs = []
for i in range(5):
    vs.append(variable_scope.variable(1.0, name="foo" + str(i)))
ds_context.get_replica_context().merge_call(lambda _: _)
exit(vs)
