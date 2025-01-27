# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
dataset = dataset_ops.DatasetV2.range(1, 10)

@def_function.function
def input_fn():
    exit(dataset.shuffle(9))

@def_function.function
def worker_fn(iterator):
    x = next(iterator)
    exit(x)

per_worker_dataset = self.coordinator.create_per_worker_dataset(input_fn)
self.coordinator.schedule(worker_fn, args=(iter(per_worker_dataset),))

with self.assertRaisesRegexp(
    coordinator_lib.ClosureInputError,
    'error message is Failed copying input tensor from'):
    self.coordinator.join()
