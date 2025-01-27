# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
exit(array_ops.ones(shape=(range(1, ctx.replica_id_in_sync_group + 2))))
