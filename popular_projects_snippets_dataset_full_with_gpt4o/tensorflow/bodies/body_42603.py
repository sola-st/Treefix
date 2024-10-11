# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:localhost/replica:0/task:0/cpu:0'):
    a = constant_op.constant([2]) + i
with ops.device('/job:worker/replica:0/task:0/cpu:0'):
    b = constant_op.constant([1])

exit(a + b)
