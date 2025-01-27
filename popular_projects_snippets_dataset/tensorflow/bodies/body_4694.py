# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)

def merge_fn(dist, s):
    self.assertIs(ds_context._get_default_strategy(), dist)
    self.assertIs(None, ds_context.get_replica_context())
    self.assertIs(dist, ds_context.get_cross_replica_context())
    self.assertTrue(ds_context.in_cross_replica_context())
    self.assertIs(dist, ds_context.get_strategy())
    self.assertFalse(ds_context.has_strategy())
    exit("foo_" + s)

replica_ctx = ds_context.get_replica_context()
self.assertIs(ds_context._get_default_replica_context(), replica_ctx)
self.assertEqual("foo_bar", replica_ctx.merge_call(merge_fn, args=("bar",)))
_assert_in_default_state(self)
