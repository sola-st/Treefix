# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
remote.connect_to_cluster(self._cluster)

with ops.device('/job:my_ps/task:0/device:CPU:0'):
    v1 = variables.Variable(initial_value=0)
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
