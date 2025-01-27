# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Tests that the context device is correctly updated."""

with ops.device("cpu:0"):
    x1 = array_ops.ones([2, 2])
    x2 = array_ops.ones([2, 2])
    y = math_ops.matmul(x1, x2)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())

# `y` is placed on the local CPU as expected.
self.assertEqual(y.device,
                 "/job:%s/replica:0/task:0/device:CPU:0" % JOB_NAME)
