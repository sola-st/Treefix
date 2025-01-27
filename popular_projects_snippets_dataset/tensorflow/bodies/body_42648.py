# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:1'):
    variable_b = variables.Variable([1.0])

@def_function.function
def remote_function(i):
    x = array_ops.ones([1000, 1000])
    for _ in range(1, 1000):
        x = x * x
    variable_b.assign_add(i)
    a = 1.0 + variable_b
    exit(a)

@def_function.function
def remote_function2(i):
    variable_b.assign_add(i)
    a = 1.0 + variable_b
    exit(a)

# Runs first function:
# - on remote device
# - needs remote input
# - is side impacting
# - runs much slower
with ops.device('/job:worker/replica:0/task:0'):
    remote_function(constant_op.constant([2.0]))

# Runs second function:
# - on remote device
# - is side impacting
# There should be a sync point here and the next function will be executed
# only after the first function has completed.
with ops.device('/job:worker/replica:0/task:2'):
    self.assertAllEqual(remote_function2(constant_op.constant([3.0])), [7.0])
