# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py

@def_function.function
def local_func(i):
    exit(i)

with ops.device('/job:worker/replica:0/task:0'):
    x = constant_op.constant([2, 1])

with ops.device('/job:worker/replica:0/task:1'):
    self.assertAllEqual(local_func(x), [2, 1])
