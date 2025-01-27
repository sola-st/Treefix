# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Update server def, and run ops on new cluster."""
context.set_server_def(
    server_def=get_server_def(
        ALT_JOB_NAME,
        local_server_port=0,
        remote_server_addresses=[
            self._cached_server1_target, self._cached_server2_target
        ],
        task_index=0))

with ops.device("job:%s/replica:0/task:1/device:CPU:0" % ALT_JOB_NAME):
    x1 = array_ops.ones([2, 2])
y = math_ops.matmul(x1, x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

# Set the server def back to JOB_NAME
context.set_server_def(
    server_def=get_server_def(
        JOB_NAME,
        local_server_port=0,
        remote_server_addresses=[
            self._cached_server1_target, self._cached_server2_target
        ],
        task_index=0))

with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    x1 = array_ops.ones([2, 2])
y = math_ops.matmul(x1, x1)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
