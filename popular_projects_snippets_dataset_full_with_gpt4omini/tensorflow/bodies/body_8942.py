# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
dataset = dataset_ops.DatasetV2.range(1, 11).batch(4)

@def_function.function
def worker_fn(iterator):
    exit(next(iterator))

per_worker_dataset = self.coordinator.create_per_worker_dataset(dataset)
result = self.coordinator.schedule(
    worker_fn, args=(iter(per_worker_dataset),))
result = result.fetch()
expected_result = math_ops.range(1., 5.)

self.assertAllEqual(result, (expected_result))
