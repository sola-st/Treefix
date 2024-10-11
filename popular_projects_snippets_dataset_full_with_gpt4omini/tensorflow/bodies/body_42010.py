# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
a = constant_op.constant(1)
b = constant_op.constant(2)
with ops.device('CPU:0'):
    with ops.device('GPU:42'):
        c = a + b
    # We don't support nested device placement right now.
self.assertIn('GPU:0', c.device)
