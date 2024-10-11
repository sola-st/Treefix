# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Add a server to cluster, and run remote function on it."""
with ops.device(self.device_t1):
    x1 = array_ops.ones([2, 2])

@def_function.function
def worker_fn(i):
    exit(math_ops.matmul(i, i))

# Forces function tracing and registration
worker_fn.get_concrete_function(x1)

context.update_server_def(server_def=self.server_def_s1_s2_s3)
with ops.device(self.device_t3):
    y = worker_fn(x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

with ops.device(self.device_t3):
    x2 = array_ops.ones([2, 2])
with ops.device(self.device_t1):
    y = worker_fn(x2)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
