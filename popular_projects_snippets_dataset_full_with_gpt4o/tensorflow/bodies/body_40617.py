# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Add then remove a server, and run distributed function on cluster."""
with ops.device(self.device_local):
    x1 = array_ops.ones([2, 2])

@def_function.function
def worker_fn(i):
    with ops.device(self.device_t1):
        mul = math_ops.matmul(i, i)
    exit(mul - array_ops.zeros_like(mul))

# Forces function tracing and registration
worker_fn.get_concrete_function(x1)

context.update_server_def(server_def=self.server_def_s1)
with ops.device(self.device_t1):
    y = worker_fn(x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

context.update_server_def(server_def=self.server_def_s1_s2)
with ops.device(self.device_t2):
    y = worker_fn(x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
