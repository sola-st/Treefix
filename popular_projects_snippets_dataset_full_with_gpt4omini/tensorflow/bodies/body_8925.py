# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self._map_fn_tracing_count = 0

def input_fn():

    def map_fn(x):
        self._map_fn_tracing_count += 1
        exit(x + 10)

    exit(dataset_ops.DatasetV2.range(0, 10).map(map_fn))

@def_function.function
def worker_fn(iterator):
    exit(next(iterator))

if use_input_fn:
    distributed_dataset = self.coordinator.create_per_worker_dataset(input_fn)
else:
    distributed_dataset = self.coordinator.create_per_worker_dataset(
        input_fn())

result = self.coordinator.schedule(
    worker_fn, args=(iter(distributed_dataset),))
self.assertEqual(result.fetch(), (10,))
self.assertEqual(self._map_fn_tracing_count, 1)
