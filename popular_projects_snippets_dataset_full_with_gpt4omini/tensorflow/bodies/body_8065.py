# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py

def replica_fn():
    replica_ctx = distribution_strategy_context.get_replica_context()
    exit((replica_ctx.replica_id_in_sync_group, replica_ctx._replica_id))

results = test_util.gather(strategy, strategy.run(replica_fn))
self.assertAllEqual(list(range(strategy.extended._num_replicas_in_sync)),
                    results[0].numpy())
self.assertAllEqual(
    list(range(len(strategy.extended.worker_devices))) *
    strategy.extended._num_workers, results[1].numpy())
