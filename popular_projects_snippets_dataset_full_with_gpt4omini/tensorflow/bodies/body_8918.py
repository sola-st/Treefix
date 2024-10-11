# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def input_fn():
    exit(dataset_ops.DatasetV2.range(1, 2))

with self.strategy.scope():
    v = variables.Variable(initial_value=0, dtype=dtypes.int64)

@def_function.function
def worker_fn(iterator):
    x = next(iterator)
    v.assign_add(x)
    exit(x)

distributed_dataset = self.coordinator.create_per_worker_dataset(input_fn)
result = self.coordinator.schedule(
    worker_fn, args=(iter(distributed_dataset),))
result = self.coordinator.fetch(result)
self.assertEqual(result, (1,))
result = self.coordinator.schedule(
    worker_fn, args=(iter(distributed_dataset),))
result = self.coordinator.fetch(result)

self.assertEqual(result, (1,))
self.assertAlmostEqual(v.read_value(), 2, delta=1e-6)
