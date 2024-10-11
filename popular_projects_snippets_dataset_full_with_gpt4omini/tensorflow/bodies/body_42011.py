# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
if test_util.is_gpu_available():
    self.skipTest('CPU only test')
with ops.device('GPU:0'):
    a = constant_op.constant(value, dtype=dtype)
self.assertIn('CPU:0', a.device)
self.assertIn('CPU:0', a.backing_device)
