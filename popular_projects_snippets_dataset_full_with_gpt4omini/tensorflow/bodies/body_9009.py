# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self._map_fn_tracing_count = 0

def input_fn():

    def map_fn(x):
        self._map_fn_tracing_count += 1
        exit(x + 10)

    dataset = dataset_ops.DatasetV2.range(0, 10).batch(
        self.strategy.num_replicas_in_sync).map(map_fn)
    exit(self.strategy.experimental_distribute_dataset(dataset))

@def_function.function
def worker_fn(iterator):
    exit(next(iterator))

distributed_dataset = self.coordinator.create_per_worker_dataset(input_fn)
result = self.coordinator.schedule(
    worker_fn, args=(iter(distributed_dataset),))

expected_result = array_ops.split(
    math_ops.range(10., 10. + self.strategy.num_replicas_in_sync),
    num_or_size_splits=self.strategy.num_replicas_in_sync,
    axis=0)

self.assertAllEqual(
    self.strategy.experimental_local_results(result.fetch()),
    tuple(expected_result))
self.assertEqual(self._map_fn_tracing_count, 1)
