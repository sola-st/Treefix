# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py

with self.strategy.scope():
    v = variables.Variable(initial_value=0, dtype=dtypes.int32)

@def_function.function
def worker_fn():
    exit((v + 1, v - 1))

remote_value = self.cluster_coord.schedule(worker_fn)

# Attempt to fetch before killing worker task should succeed.
fetched = remote_value.get()[0]
self.assertIsInstance(fetched, ops.Tensor)
self.assertEqual(fetched.device, "/job:chief/replica:0/task:0/device:CPU:0")
self.assertEqual((1, -1), remote_value.get())
remote_value.get()[0].numpy()

# As well as the remote tensors that point to worker0 or worker1.
values = remote_value._values[0]
self.assertIsInstance(values, ops.Tensor)
self.assertRegex(values.device,
                 "/job:worker/replica:0/task:[0-1]/device:CPU:0")
self.assertEqual((1, -1), remote_value._values)
remote_value._values[0].numpy()

# Terminate the workers and wait a little so that they are indeed killed.
for i in range(self.num_workers):
    self._cluster.kill_task("worker", i)
time.sleep(5)

# Attempt to fetch after killing worker tasks should succeed as well.
remote_value.get()[0].numpy()
self.assertEqual((1, -1), remote_value.get())

# Attempting to copy the tensor from worker now should fail.
with self.assertRaises(errors.UnavailableError) as cm:
    remote_value._values[0].numpy()
self.assertIn("failed to connect to all addresses", cm.exception.message)
self.assertIn("/job:worker/replica:0/task:", cm.exception.message)
