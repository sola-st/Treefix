# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
"""A mini stress test for streaming - issuing many RPCs back to back."""
with ops.device('job:worker/replica:0/task:0/device:CPU:0'):
    x = array_ops.ones([2, 2])
    y = array_ops.zeros([2, 2])
    num_iters = 200
    for _ in range(num_iters):
        y = x + y
        # Ask for y's shape after every 10 additions on average.
        # This exercises waiting for remote shape logic in TensorHandle.
        if random.randint(1, 10) == 1:
            _ = y.shape
np.testing.assert_array_equal(
    [[num_iters, num_iters], [num_iters, num_iters]], y.numpy())
