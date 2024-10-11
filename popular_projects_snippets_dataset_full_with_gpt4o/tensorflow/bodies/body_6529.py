# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    v = variable_scope.variable(1.0)
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v)

with distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    self._test_mv_properties(result, "Variable:0", distribution)
