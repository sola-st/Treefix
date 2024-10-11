# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
a = constant_op.constant(1)
b = constant_op.constant(2)
c = a + b
with ops.device('CPU'):
    d = a + b
self.assertIn('GPU', c.device)
self.assertIn('CPU', d.device)
