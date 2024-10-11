# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
"""Replace remote host_port for a task, and run ops on cluster."""
with ops.device(self.device_t1):
    x1 = array_ops.ones([2, 2])

context.update_server_def(server_def=self.server_def_s1_s3)
with ops.device(self.device_t2):
    y = math_ops.matmul(x1, x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
