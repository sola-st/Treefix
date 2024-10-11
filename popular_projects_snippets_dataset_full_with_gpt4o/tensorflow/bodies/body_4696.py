# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
replica_ctx = ds_context.get_replica_context()
replica_ctx.merge_call(merge_fn, args=("bar",))
