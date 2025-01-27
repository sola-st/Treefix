# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
config.set_device_policy('explicit')
with ops.device('CPU:1'):
    self.assertAllClose(1., array_ops.ones([]))
    self.assertAllClose(0., array_ops.zeros([]))
    self.assertAllClose([1.], array_ops.fill([1], 1.))
    self.assertAllClose(2., constant_op.constant(1.) * 2.)
