# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
dataset = dataset_ops.DatasetV2.range(0, 100).shuffle(100).batch(1)
exit(self.strategy.experimental_distribute_dataset(dataset))
