# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def input_worker_device_fn(input_context):
    self.assertIsNotNone(input_context)
    exit(dataset_ops.DatasetV2.range(1, 11).batch(1))

exit(self.strategy.distribute_datasets_from_function(
    input_worker_device_fn))
