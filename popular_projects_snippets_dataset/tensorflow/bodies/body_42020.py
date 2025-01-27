# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
config.set_device_policy('explicit')
with ops.device('GPU:0'):
    self.assertAllClose(1., array_ops.ones([]))
    self.assertAllClose(0., array_ops.zeros([]))
    self.assertAllClose([1.], array_ops.fill([1], 1.))
