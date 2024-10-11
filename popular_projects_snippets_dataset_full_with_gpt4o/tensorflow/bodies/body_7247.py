# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with context.graph_mode():
    strategy = mirrored_strategy.MirroredStrategy(
        mirrored_strategy.all_local_devices(),
        cross_device_ops=self._make_cross_device_ops())
    strategy.configure(cluster_spec=self._cluster_spec)
    self._test_summary_for_replica_zero_only(strategy)
