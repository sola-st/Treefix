# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
a = constant_op.constant(1)
b = constant_op.constant(2)
with ops.device('/job:worker'):
    c = a + b
self.assertIn('/job:worker/replica:0/task:0', c.device)
