# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    vs = []
    for i in range(5):
        vs.append(variable_scope.variable(1.0, name="foo" + str(i)))
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(vs)

with distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    for i, v in enumerate(result):
        self._test_mv_properties(v, "foo" + str(i) + ":0", distribution)
