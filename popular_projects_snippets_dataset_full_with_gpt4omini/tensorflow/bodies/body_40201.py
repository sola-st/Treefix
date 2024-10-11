# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Basic server connection."""
context._reset_context()
remote.connect_to_remote_host(self._cached_server1_target)

with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
    x1 = array_ops.ones([2, 2])
    x2 = array_ops.ones([2, 2])
    y = math_ops.matmul(x1, x2)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
