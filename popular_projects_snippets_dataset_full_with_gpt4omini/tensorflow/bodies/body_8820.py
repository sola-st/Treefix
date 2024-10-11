# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
exit(self.cluster_coord.strategy.distribute_datasets_from_function(
    lambda _: dataset_fn()))
