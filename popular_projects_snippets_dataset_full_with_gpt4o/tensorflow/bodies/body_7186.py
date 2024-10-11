# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def model_fn():
    v = variable_scope.variable(1.0, name="foo")
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v)

with distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    self.assertTrue(distribute_utils.is_mirrored(result))
    self.assertEqual("foo:0", result.name)
