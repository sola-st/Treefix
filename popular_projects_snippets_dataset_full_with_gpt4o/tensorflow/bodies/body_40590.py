# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Add a server to cluster, and run remote ops on it."""
with ops.device(self.device_t1):
    x1 = array_ops.ones([2, 2])

context.update_server_def(server_def=self.server_def_s1_s2_s3)
with ops.device(self.device_t3):
    x2 = array_ops.ones([2, 2])

# Test new server accessing resources on old server
with ops.device(self.device_t3):
    y = math_ops.matmul(x1, x2)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

# Test old server accessing resources on new server
with ops.device(self.device_t2):
    y = math_ops.matmul(x1, x2)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
