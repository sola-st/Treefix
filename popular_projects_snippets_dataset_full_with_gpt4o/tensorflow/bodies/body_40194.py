# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Basic remote eager execution with defun."""

mm_defun = def_function.function(math_ops.matmul)
with ops.device("job:%s/replica:0/task:1/device:CPU:0" % JOB_NAME):
    x1 = array_ops.ones([2, 2])
with ops.device("job:%s/replica:0/task:2/device:CPU:0" % JOB_NAME):
    x2 = array_ops.ones([2, 2])
    y = mm_defun(x1, x2)
np.testing.assert_array_equal([[2, 2], [2, 2]], y.numpy())
