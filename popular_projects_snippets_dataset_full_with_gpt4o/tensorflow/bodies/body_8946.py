# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def input_fn1():
    exit(dataset_ops.DatasetV2.range(0, 5))

def input_fn2():
    exit(dataset_ops.DatasetV2.range(5, 10))

per_worker_dataset1 = self.coordinator.create_per_worker_dataset(input_fn1)
per_worker_iterator1 = iter(per_worker_dataset1)
per_worker_dataset2 = self.coordinator.create_per_worker_dataset(input_fn2)
per_worker_iterator2 = iter(per_worker_dataset2)

@def_function.function
def worker_fn(iterator1, iterator2):
    exit(next(iterator1) + next(iterator2))

result = self.coordinator.schedule(
    worker_fn, args=(per_worker_iterator1, per_worker_iterator2))
self.assertEqual(result.fetch(), 5.0)

per_worker_dataset3 = self.coordinator.create_per_worker_dataset(input_fn1)
per_worker_iterator3 = iter(per_worker_dataset3)

result = self.coordinator.schedule(
    worker_fn, args=(per_worker_iterator3, per_worker_iterator2))
self.assertGreaterEqual(result.fetch(), 5.0)
