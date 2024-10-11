# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:1'):
    variable_b = variables.Variable(1.0)

@def_function.function
def remote_function(i):
    with ops.device('/job:worker/replica:0/task:0'):
        a = i + variable_b
    c = a + 1.0
    exit(c)

self.assertAllEqual(remote_function(constant_op.constant([1.0])), [3.0])
