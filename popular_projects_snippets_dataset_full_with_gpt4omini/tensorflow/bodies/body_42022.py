# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
with ops.device(device):
    a = constant_op.constant(value, dtype=dtype)
    self.assertIn(device, a.device)
