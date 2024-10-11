# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
with ops.device("gpu:0"):
    x = array_ops.ones([2, 2])
with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    y = math_ops.matmul(x, x)

np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
