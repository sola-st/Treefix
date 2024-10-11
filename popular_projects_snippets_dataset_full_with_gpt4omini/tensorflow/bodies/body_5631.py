# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(strategy, 0., enable_packed_handle)

@tf_function
def update_device0():
    with ops.device(strategy.extended.parameter_devices[0]):
        v.assign(1.)

@tf_function
def update_device1():
    with ops.device(strategy.extended.parameter_devices[1]):
        v.assign(2.)

update_device0()
update_device1()
self.assertReplica(v, [1., 2.])

with ops.device("CPU:0"):
    # Update the primary replica.
    v.assign(3.)
    self.assertReplica(v, [3., 2.])
