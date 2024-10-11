# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
dataset = dataset_ops.DatasetV2.range(1, 11).batch(4)
exit(self.strategy.experimental_distribute_dataset(dataset))
