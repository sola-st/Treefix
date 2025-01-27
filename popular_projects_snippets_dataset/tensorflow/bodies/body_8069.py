# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
exit(math_ops.cast(
    distribution_strategy_context.get_replica_context()
    .replica_id_in_sync_group, dtypes.float32))
