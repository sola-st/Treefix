# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
exit(ds_context.get_replica_context().merge_call(merge_fn, args=(i,)))
