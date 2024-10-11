# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
device_ids = self.device.unpack(self.device.device_ids)
self.assertAllClose([0, 1], device_ids)
# TODO(allenl): Should device IDs be int64 so they can be placed on GPUs?
# Currently backing_device is CPU.
self.assertIn(self.device.components[0], device_ids[0].device)
self.assertIn(self.device.components[1], device_ids[1].device)
