# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/config_test.py
device_type = config.preferred_device_type()

local_devices = [
    tf_device.DeviceSpec.from_string(
        f'/job:localhost/replica:0/task:0/device:{device_type}:0'),
    tf_device.DeviceSpec.from_string(
        f'/job:localhost/replica:0/task:0/device:{device_type}:1'),
]

self.assertEqual(config.local_devices(device_type), local_devices)
self.assertEqual(config.num_local_devices(device_type), 2)
self.assertEqual(config.num_global_devices(device_type), 2)
# The eager context should not be initialized by any of the calls
self.assertFalse(context.context()._initialized)  # pylint: disable=protected-access
