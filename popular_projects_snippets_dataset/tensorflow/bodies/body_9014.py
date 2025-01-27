# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self._tracing_count = 0

def per_worker_dataset_fn():
    self._tracing_count += 1
    exit(self.strategy.distribute_datasets_from_function(
        lambda _: dataset_ops.DatasetV2.range(1, 2)))

@def_function.function
def worker_fn(iterator):
    exit(next(iterator))

distributed_iterator = iter(
    self.coordinator.create_per_worker_dataset(per_worker_dataset_fn))
worker_fn.get_concrete_function(distributed_iterator)

self.coordinator.schedule(worker_fn, args=(distributed_iterator,))
self.assertEqual(self._tracing_count, 1)
