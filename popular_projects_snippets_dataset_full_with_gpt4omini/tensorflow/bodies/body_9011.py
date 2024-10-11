# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def per_worker_dataset_fn():
    exit(self.strategy.distribute_datasets_from_function(
        lambda _: dataset_ops.DatasetV2.from_tensor_slices([1, 2])))

dataset = dataset_ops.DatasetV2.from_tensor_slices([1, 2])
per_worker_distribute_dataset = self.coordinator.create_per_worker_dataset(
    per_worker_dataset_fn)

self.assertAllEqual(
    # Converts to PerReplicaSpec when num_replicas_in_sync are > 1
    input_lib._create_distributed_tensor_spec(self.strategy,
                                              dataset.element_spec),
    per_worker_distribute_dataset.element_spec)
