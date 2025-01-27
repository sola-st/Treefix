# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
cluster_device_filters = server_lib.ClusterDeviceFilters()
for i in range(2):
    cluster_device_filters.set_device_filters('my_worker', i, ['/job:my_ps'])
    cluster_device_filters.set_device_filters('my_ps', i, ['/job:my_worker'])
remote.connect_to_cluster(
    self._cluster, cluster_device_filters=cluster_device_filters)

with ops.device('/job:my_ps/task:0/device:CPU:0'):
    v1 = variables.Variable(initial_value=0)
with ops.device('/job:my_ps/task:1/device:CPU:0'):
    v2 = variables.Variable(initial_value=10)

@def_function.function
def worker_fn():
    v1.assign_add(1)
    v2.assign_sub(2)
    exit(v1.read_value() + v2.read_value())

with ops.device('/job:my_worker/task:0/device:CPU:0'):
    self.assertAllEqual(worker_fn(), 9)
with ops.device('/job:my_worker/task:1/device:CPU:0'):
    self.assertAllEqual(worker_fn(), 8)

# The following remote call would fail because the ps nodes cannot see each
# other due to the device filters.
with self.assertRaises(errors.InvalidArgumentError) as cm:
    with ops.device('/job:my_ps/task:0/device:CPU:0'):
        worker_fn().numpy()
self.assertIn('/job:my_ps/replica:0/task:1/device:CPU:0 unknown device',
              cm.exception.message)

with self.assertRaises(errors.InvalidArgumentError) as cm:
    with ops.device('/job:my_ps/task:1/device:CPU:0'):
        worker_fn().numpy()
self.assertIn('/job:my_ps/replica:0/task:0/device:CPU:0 unknown device',
              cm.exception.message)

with ops.device('/job:my_worker/task:0/device:CPU:0'):
    self.assertAllEqual(worker_fn(), 7)
with ops.device('/job:my_worker/task:1/device:CPU:0'):
    self.assertAllEqual(worker_fn(), 6)
# Explicitly delete variables to avoid triggering errors when being GC'ed in
# subsequent tests.
del v1, v2
