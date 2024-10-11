# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Remote eager weight read in a tape."""

with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    w = resource_variable_ops.ResourceVariable([[3.0]])
    with backprop.GradientTape() as tape:
        loss = w * w

    grad = tape.gradient(loss, w)
np.testing.assert_array_equal([[9.0]], loss.numpy())
np.testing.assert_array_equal([[6.0]], grad.numpy())
