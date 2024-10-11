# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
for device in self.backend.local_devices():
    self.assertEqual(device.platform, self.backend.platform)
