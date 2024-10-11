# Extracted from ./data/repos/tensorflow/tensorflow/python/client/device_lib_test.py
devices = device_lib.list_local_devices()
self.assertGreater(len(devices), 0)
self.assertEqual(devices[0].device_type, "CPU")

devices = device_lib.list_local_devices(config_pb2.ConfigProto())
self.assertGreater(len(devices), 0)
self.assertEqual(devices[0].device_type, "CPU")

# GPU test
if test.is_gpu_available():
    self.assertGreater(len(devices), 1)
    self.assertIn("GPU", [d.device_type for d in devices])
