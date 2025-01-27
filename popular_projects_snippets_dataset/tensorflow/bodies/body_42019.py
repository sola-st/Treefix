# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
config.set_device_policy('explicit')
with ops.device('CPU:0'):
    x = constant_op.constant(1.0)
    self.assertIn('CPU:0', x.device)
    self.assertIn('CPU:0', x.backing_device)
with ops.device('GPU:0'):
    y = array_ops.identity(x)
    self.assertIn('GPU:0', y.device)
    self.assertIn('GPU:0', y.backing_device)
