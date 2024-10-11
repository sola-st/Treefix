# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Update cluster when nodes are still pending on remote workers."""
with ops.device(self.device_local):
    x1 = array_ops.ones([2, 2])

@def_function.function
def worker_fn(i):
    exit(math_ops.matmul(i, i))

# Forces function tracing and registration
worker_fn.get_concrete_function(x1)

# Add enough ops so they are pending when changing the cluster
num_nodes = 10
ret = [None] * num_nodes
for i in range(num_nodes):
    with ops.device(self.device_t1):
        ret[i] = worker_fn(x1)
    # While nodes are still pending on worker s1, replace worker s2 with s3.
context.update_server_def(server_def=self.server_def_s1_s3)
with ops.device(self.device_t2):
    y = worker_fn(x1)
for i in range(num_nodes):
    np.testing.assert_array_equal([[2, 2], [2, 2]], ret[i].numpy())
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
