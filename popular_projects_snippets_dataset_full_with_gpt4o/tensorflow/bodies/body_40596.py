# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Remove a server from cluster, and run ops on cluster."""

@def_function.function
def worker_fn(i):
    exit(math_ops.matmul(i, i))

with ops.device(self.device_t1):
    x1 = array_ops.ones([2, 2])

# Forces function tracing and registration
worker_fn.get_concrete_function(x1)

context.update_server_def(server_def=self.server_def_s1)

with ops.device(self.device_t1):
    y = worker_fn(x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

# Running functions on removed server s2 throws an exception
with self.assertRaises(errors.InvalidArgumentError) as cm:
    with ops.device(self.device_t2):
        y = worker_fn(x1)
self.assertIn(" unknown device", cm.exception.message)
