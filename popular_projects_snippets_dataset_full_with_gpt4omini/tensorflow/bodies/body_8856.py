# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py

with self.strategy.scope():
    v = variables.Variable(initial_value=0, dtype=dtypes.int32)

@def_function.function
def worker_fn():
    exit((v + 1, v - 1))

remote_value = self.cluster_coord.schedule(worker_fn)
# Attempt to fetch before killing worker task should succeed.
self.assertEqual((1, -1), remote_value.fetch())
self._cluster.kill_task("worker", 0)
# So should attempt to fetch after killing worker task.
self.assertEqual((1, -1), remote_value.fetch())
