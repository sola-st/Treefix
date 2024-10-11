# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:0/cpu:0'):
    variable_b = variables.Variable(1)

# Add a sync point to avoid the out-of-order issue of eager async execution
# (b/155789951).
context.async_wait()

@def_function.function
def with_variable(i):
    exit(i + variable_b)

self.assertAllEqual(with_variable(constant_op.constant([2])).numpy(), [3])
