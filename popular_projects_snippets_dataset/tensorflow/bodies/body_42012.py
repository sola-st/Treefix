# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
with ops.device('GPU:0'):
    a = math_ops.add(constant_op.constant(value, dtype=dtype),
                     constant_op.constant(value, dtype=dtype))
self.assertIn(expect, a.backing_device)
