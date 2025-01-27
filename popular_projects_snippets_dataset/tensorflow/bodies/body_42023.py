# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
if not test_util.is_gpu_available():
    self.skipTest('Test requires a GPU')
with ops.device(device):
    a = constant_op.constant(value, dtype=dtype)
    self.assertIn(device, a.device)
    if a.dtype == dtypes.float32:
        self.assertIn(device, a.backing_device)
