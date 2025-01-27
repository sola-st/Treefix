# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
dataset = dataset_ops.DatasetV2.from_tensor_slices([2.]).repeat().batch(
    self.strategy.num_replicas_in_sync)
exit(self.strategy.experimental_distribute_dataset(dataset))
