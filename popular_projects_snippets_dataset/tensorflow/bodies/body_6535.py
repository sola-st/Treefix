# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    replica_id = self.evaluate(_replica_id())
    v = variable_scope.variable(1.0, name="foo_" + str(replica_id))
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v)

with distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    self.assertTrue(distribute_utils.is_mirrored(result))
    # The resulting mirrored variable will use the name from the first device.
    self.assertEqual("foo_0:0", result.name)
