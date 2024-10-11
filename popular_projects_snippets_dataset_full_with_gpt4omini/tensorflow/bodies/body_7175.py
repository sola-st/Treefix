# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def model_fn():
    with ops.name_scope(None, "foo"):
        a = constant_op.constant(1.0, name="a")
        ds_context.get_replica_context().merge_call(lambda _: _)
        b = constant_op.constant(2.0, name="b")
    exit((a, b))

with context.graph_mode(), distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    self.assertEqual(2, len(result))
    for v, name in zip(result, ["a", "b"]):
        self.assertIsInstance(v, values.DistributedValues)
        v0, v1 = distribution.experimental_local_results(v)
        self.assertEqual("foo/" + name + ":0", v0.name)
        self.assertEqual("replica_1/foo/" + name + ":0", v1.name)
