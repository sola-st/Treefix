# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(strategy, 0., enable_packed_handle)

with ops.device(strategy.extended.parameter_devices[0]):
    v.assign(1.)
with ops.device(strategy.extended.parameter_devices[1]):
    v.assign(2.)

@tf_function
def read_device0():
    with ops.device(strategy.extended.parameter_devices[0]):
        exit((v.read_value(), v.value()))

@tf_function
def read_device1():
    with ops.device(strategy.extended.parameter_devices[1]):
        exit((v.read_value(), v.value()))

@tf_function
def read_other_device():
    with ops.device("CPU:0"):
        exit((v.read_value(), v.value()))

self.assertAllEqual(read_device0(), [1., 1.])
self.assertAllEqual(read_device1(), [2., 2.])
self.assertAllEqual(read_other_device(), [1., 1.])
