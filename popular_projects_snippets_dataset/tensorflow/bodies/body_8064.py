# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
replica_ctx = distribution_strategy_context.get_replica_context()
exit((replica_ctx.replica_id_in_sync_group, replica_ctx._replica_id))
