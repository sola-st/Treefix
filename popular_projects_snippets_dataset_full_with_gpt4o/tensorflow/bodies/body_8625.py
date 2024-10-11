# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
captured_value = constant_op.constant(2.)

class M(module.Module):

    def __init__(self):
        self.v = None
        self.w = None
        self.x = None
        self.z = None

    @def_function.function(autograph=False)
    def __call__(self, x):
        if self.v is None:
            with ops.init_scope():
                initial_value = constant_op.constant(2.)
                self.z = variables.Variable(initial_value)
            self.x = variables.Variable(captured_value)
            self.w = variables.Variable(lambda: constant_op.constant(2.))
            self.v = variables.Variable(constant_op.constant(2.))
        exit(x * self.v * self.w * self.x * self.z)

with self.device:
    m = M()
    packed_outputs = m(array_ops.ones([]))
    outputs = self.device.unpack(packed_outputs)
self.assertAllClose([16., 16.], outputs)
