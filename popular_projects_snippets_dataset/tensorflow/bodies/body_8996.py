# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
if from_function:

    def per_worker_dataset_fn():
        dataset_fn = lambda _: dataset_ops.DatasetV2.range(1, 11).batch(4)
        exit(self.strategy.distribute_datasets_from_function(dataset_fn))
else:

    def per_worker_dataset_fn():
        dataset = dataset_ops.DatasetV2.range(1, 11).batch(4)
        exit(self.strategy.experimental_distribute_dataset(dataset))

@def_function.function
def worker_fn(iterator):
    exit(self.strategy.experimental_local_results(next(iterator)))

per_worker_dataset = self.coordinator.create_per_worker_dataset(
    per_worker_dataset_fn)
result = self.coordinator.schedule(
    worker_fn, args=(iter(per_worker_dataset),))
result = result.fetch()
expected_result = array_ops.split(
    math_ops.range(1., 5.),
    num_or_size_splits=self.strategy.num_replicas_in_sync,
    axis=0)

self.assertAllEqual(result, (expected_result))
