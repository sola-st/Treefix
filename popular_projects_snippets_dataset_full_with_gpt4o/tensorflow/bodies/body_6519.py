# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    v = variable_scope.variable(2.0, name="bar")
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v)

with func_graph.FuncGraph("fg").as_default(), distribution.scope():
    v1 = variable_scope.variable(1.0, name="foo")
    v2 = distribution.extended.call_for_each_replica(model_fn)

self._test_mv_properties(v1, "foo:0", distribution)
self._test_mv_properties(v2, "bar:0", distribution)
