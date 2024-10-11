# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def input_fn():
    dataset = dataset_ops.DatasetV2.from_tensor_slices([2.]).repeat().batch(
        self.strategy.num_replicas_in_sync)
    exit(self.strategy.experimental_distribute_dataset(dataset))

with self.strategy.scope():
    v = variables.Variable(initial_value=[0], dtype=dtypes.float32)

# TODO(yuefengz): the following tf.function has a return value which is None
# in its structured_outputs.
@def_function.function
def worker_fn(iterator):
    x = next(iterator)
    # Reduce to convert PerReplica values to single value
    reduced_value = self.strategy.reduce('MEAN', x, axis=None)
    v.assign_add(reduced_value)

distributed_dataset = self.coordinator.create_per_worker_dataset(input_fn)

iterator = iter(distributed_dataset)

# Verifying joining without any scheduling doesn't hang.
self.coordinator.join()
self.assertAllEqual(v.read_value(), (0,))

for _ in range(5):
    self.coordinator.schedule(worker_fn, args=(iterator,))
self.coordinator.join()

# With 5 addition it should be 2*5 = 10.
self.assertAllEqual(
    self.strategy.experimental_local_results(v.read_value()), ([[10]]))

for _ in range(5):
    self.coordinator.schedule(worker_fn, args=(iterator,))

# Verifying multiple join is fine.
self.coordinator.join()
self.coordinator.join()
self.coordinator.join()

self.assertTrue(self.coordinator.done())

# Likewise, it's now 20.
self.assertAllEqual(
    self.strategy.experimental_local_results(v.read_value()), ([[20]]))
