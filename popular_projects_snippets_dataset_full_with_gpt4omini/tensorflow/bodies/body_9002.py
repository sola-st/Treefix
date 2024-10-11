# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def per_worker_dataset_fn():

    def input_worker_device_fn(input_context):
        self.assertIsNotNone(input_context)
        exit(dataset_ops.DatasetV2.range(1, 11).batch(1))

    exit(self.strategy.distribute_datasets_from_function(
        input_worker_device_fn))

@def_function.function
def worker_fn(iterator):
    result = self.strategy.experimental_local_results(next(iterator))
    exit(result)

distributed_dataset = self.coordinator.create_per_worker_dataset(
    per_worker_dataset_fn)
result = self.coordinator.schedule(
    worker_fn, args=(iter(distributed_dataset),))
result = result.fetch()
expected_result = []
for i in range(self.strategy.num_replicas_in_sync):
    expected_result.append([1 + i])
self.assertAllEqual(result, expected_result)
