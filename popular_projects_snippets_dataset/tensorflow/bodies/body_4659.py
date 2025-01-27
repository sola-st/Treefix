# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
t.assertIs(ds_context._get_default_replica_context(),
           ds_context.get_replica_context())
t.assertIs(None, ds_context.get_cross_replica_context())
t.assertFalse(ds_context.in_cross_replica_context())
t.assertIs(ds_context._get_default_strategy(), ds_context.get_strategy())
t.assertFalse(ds_context.has_strategy())
