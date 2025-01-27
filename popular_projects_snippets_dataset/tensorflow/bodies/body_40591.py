# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Remove a server from cluster, and run ops on cluster."""
with ops.device(self.device_t1):
    x1 = array_ops.ones([2, 2])
with ops.device(self.device_t2):
    x2 = array_ops.ones([2, 2])

with ops.device(self.device_t1):
    y = math_ops.matmul(x1, x2)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

context.update_server_def(server_def=self.server_def_s1)
with ops.device(self.device_t1):
    y = math_ops.matmul(x1, x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

# Running ops on removed server s2 throws an exception
with self.assertRaises(errors.InvalidArgumentError) as cm:
    with ops.device(self.device_t2):
        y = math_ops.matmul(x1, x2)
self.assertIn("unknown device", cm.exception.message)
