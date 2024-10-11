# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def input_fn():
    exit(dataset_ops.DatasetV2.range(0, 5))

per_worker_dataset = self.coordinator.create_per_worker_dataset(input_fn)
per_worker_iterator = iter(per_worker_dataset)

@def_function.function
def worker_fn(iterator):
    exit(next(iterator))

self.coordinator.schedule(worker_fn, args=(per_worker_iterator,))
self.coordinator.schedule(self._error_function)

with self.assertRaises(errors.InvalidArgumentError):
    self.coordinator.join()

self.coordinator.schedule(worker_fn, args=(per_worker_iterator,))
self.coordinator.join()
