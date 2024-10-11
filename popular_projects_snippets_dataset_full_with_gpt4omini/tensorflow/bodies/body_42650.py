# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:1'):
    variable_b = variables.Variable(1.0)

@def_function.function
def remote_function(i):
    with ops.device('/job:worker/replica:0/task:0'):
        a = i + variable_b
    c = a + 1.0
    exit(c)

with ops.device('/job:worker/replica:0/task:0'):
    self.assertAllEqual(remote_function(constant_op.constant([1.0])), [3.0])

if test_util.is_gpu_available():
    with ops.device('/job:worker/replica:0/task:0/device:GPU:0'):
        self.assertAllEqual(remote_function(constant_op.constant([1.0])), [3.0])
