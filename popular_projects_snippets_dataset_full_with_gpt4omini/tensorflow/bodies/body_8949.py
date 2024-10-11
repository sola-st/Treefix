# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def input_fn():
    exit(dataset_ops.DatasetV2.range(1, 100))

per_worker_dataset1 = self.coordinator.create_per_worker_dataset(input_fn)
per_worker_dataset2 = self.coordinator.create_per_worker_dataset(input_fn)

@def_function.function
def worker_fn(iterator1, iterator2):
    exit(next(iterator1) + next(iterator2))

for _ in range(10):
    per_worker_iterator1 = iter(per_worker_dataset1)
    per_worker_iterator2 = iter(per_worker_dataset2)
    result = self.coordinator.schedule(
        worker_fn, args=(per_worker_iterator1, per_worker_iterator2))
    for _ in range(10):
        self.coordinator.schedule(
            worker_fn, args=(per_worker_iterator1, per_worker_iterator2))
    self.coordinator.join()
    self.assertGreaterEqual(result.fetch(), 2.0)
del per_worker_iterator1, per_worker_iterator2
gc.collect()

# There shouldn't be any live iterator objects.
for w in self.coordinator._cluster.workers:
    for r in w._resource_remote_value_refs:
        self.assertIsNone(r())
