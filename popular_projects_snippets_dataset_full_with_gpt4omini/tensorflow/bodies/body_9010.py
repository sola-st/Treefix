# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
exit(self.strategy.distribute_datasets_from_function(
    lambda _: dataset_ops.DatasetV2.from_tensor_slices([1, 2])))
