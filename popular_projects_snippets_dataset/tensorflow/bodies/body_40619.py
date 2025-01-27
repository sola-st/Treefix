# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Tests that replacing servers works correctly.

    We create two servers, t1 and t2. We first replace t2, then we replace t1.

    Among other things, this ensures that both already existing, and
    restarted workers have the context view IDs correctly updated.
    """
with ops.device(self.device_local):
    x1 = array_ops.ones([2, 2])

@def_function.function
def worker_fn(i):
    with ops.device(self.device_t1):
        mul = math_ops.matmul(i, i)
    with ops.device(self.device_t2):
        add = mul + i
    exit(add - i)

# Forces function tracing and registration
worker_fn.get_concrete_function(x1)

# Replace task2
context.update_server_def(server_def=self.server_def_s1_s3)
for device in (self.device_t1, self.device_t2):
    with ops.device(device):
        y = worker_fn(x1)
    np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

# Then replace task1
context.update_server_def(server_def=self.server_def_s4_s3)
for device in (self.device_t1, self.device_t2):
    with ops.device(device):
        y = worker_fn(x1)
    np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
