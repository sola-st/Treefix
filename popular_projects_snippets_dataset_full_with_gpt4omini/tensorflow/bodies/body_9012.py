# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self._tracing_count += 1
exit(self.strategy.distribute_datasets_from_function(
    lambda _: dataset_ops.DatasetV2.range(1, 2)))
