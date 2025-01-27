# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
if test_util.is_xla_enabled():
    self.skipTest('Assign_add is not deterministic across threads in XLA')

def input_fn():
    exit(dataset_ops.DatasetV2.from_tensor_slices([2] * 10))

with self.strategy.scope():
    v = variables.Variable(initial_value=0, dtype=dtypes.int32)

# TODO(yuefengz): the following tf.function has a return value which is None
# in its structured_outputs.
@def_function.function
def worker_fn(iterator):
    x = next(iterator)
    v.assign_add(x)

distributed_dataset = self.coordinator.create_per_worker_dataset(input_fn)

iterator = iter(distributed_dataset)

# Verifying joining without any scheduling doesn't hang.
self.coordinator.join()
self.assertEqual(v.read_value().numpy(), 0)

for _ in range(5):
    self.coordinator.schedule(worker_fn, args=(iterator,))
self.coordinator.join()

# With 5 addition it should be 2*5 = 10.
self.assertEqual(v.read_value().numpy(), 10)

for _ in range(5):
    self.coordinator.schedule(worker_fn, args=(iterator,))

# Verifying multiple join is fine.
self.coordinator.join()
self.coordinator.join()
self.coordinator.join()

self.assertTrue(self.coordinator.done())

# Likewise, it's now 20.
self.assertEqual(v.read_value().numpy(), 20.)
