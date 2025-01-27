# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Basic remote eager weight read."""

with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    w = resource_variable_ops.ResourceVariable([[2.0]])
    loss = w * w
np.testing.assert_array_equal([[4.0]], loss.numpy())
