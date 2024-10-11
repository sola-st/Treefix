# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Tests that the remote copy happens satisfactorily."""
x1 = array_ops.ones([2, 2]).gpu()
with ops.device("/job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    x2 = x1._copy()  # pylint: disable=protected-access

np.testing.assert_array_equal(x1.numpy(), x2.numpy())
