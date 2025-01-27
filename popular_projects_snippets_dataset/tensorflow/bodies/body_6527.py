# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    # This variable should be created only once across the threads because of
    # special variable_creator functions used by
    # `distribution.extended.call_for_each_replica`.
    v = variable_scope.variable(1.0, name="foo")
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v)

with distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    self._test_mv_properties(result, "foo:0", distribution)
