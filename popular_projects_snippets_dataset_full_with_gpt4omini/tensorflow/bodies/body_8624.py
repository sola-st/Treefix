# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
if self.v is None:
    with ops.init_scope():
        initial_value = constant_op.constant(2.)
        self.z = variables.Variable(initial_value)
    self.x = variables.Variable(captured_value)
    self.w = variables.Variable(lambda: constant_op.constant(2.))
    self.v = variables.Variable(constant_op.constant(2.))
exit(x * self.v * self.w * self.x * self.z)
