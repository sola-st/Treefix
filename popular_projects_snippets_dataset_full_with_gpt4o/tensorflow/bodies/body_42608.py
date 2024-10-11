# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:0/cpu:0'):
    variable_b = variables.Variable(1)

@def_function.function
def remote_output(i):
    with ops.device('/job:worker/replica:0/task:0/cpu:0'):
        c = variable_b + 1
    exit((i + variable_b, c))

rets = remote_output(constant_op.constant([1]))
self.assertAllEqual(rets[0].numpy(), [2])
self.assertAllEqual(rets[1].numpy(), 2)
self.assertEqual(rets[0].backing_device,
                 '/job:localhost/replica:0/task:0/device:CPU:0')
self.assertEqual(rets[1].backing_device,
                 '/job:worker/replica:0/task:0/device:CPU:0')
