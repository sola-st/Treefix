# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def replica_fn():
    value = math_ops.cast(
        distribution_strategy_context.get_replica_context()
        .replica_id_in_sync_group + 1, v.dtype)
    v.assign(value)

self.strategy.run(replica_fn)
