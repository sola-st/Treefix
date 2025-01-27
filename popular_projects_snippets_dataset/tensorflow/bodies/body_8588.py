# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with self.device:
    c = constant_op.constant(1.)
    d = constant_op.constant(2.)
    e = c + d
    outputs = self.device.unpack(e)
self.assertAllClose([3., 3.], outputs)

self.assertIn(self.device.components[0], outputs[0].backing_device)
self.assertIn(self.device.components[1], outputs[1].backing_device)
