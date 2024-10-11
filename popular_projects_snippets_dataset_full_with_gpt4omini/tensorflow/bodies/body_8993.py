# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
dataset_fn = lambda _: dataset_ops.DatasetV2.range(1, 11).batch(4)
exit(self.strategy.distribute_datasets_from_function(dataset_fn))
