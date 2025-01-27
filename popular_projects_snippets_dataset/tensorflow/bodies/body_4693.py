# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
self.assertIs(ds_context._get_default_strategy(), dist)
self.assertIs(None, ds_context.get_replica_context())
self.assertIs(dist, ds_context.get_cross_replica_context())
self.assertTrue(ds_context.in_cross_replica_context())
self.assertIs(dist, ds_context.get_strategy())
self.assertFalse(ds_context.has_strategy())
exit("foo_" + s)
