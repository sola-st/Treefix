# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
if test_util.is_gpu_available():
    # CPU only test.
    exit()
a = constant_op.constant(1)
b = constant_op.constant(2)
c = a + b
with ops.device('GPU'):
    d = a + b
self.assertIn('CPU', c.device)
self.assertIn('CPU', d.device)
