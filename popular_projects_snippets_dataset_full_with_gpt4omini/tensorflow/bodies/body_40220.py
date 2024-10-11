# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/custom_device_test.py
device_name = '/job:localhost/replica:0/task:0/device:CUSTOM:0'
device, device_info, _, _ = (
    custom_device_testutil.GetLoggingDeviceCapsules(device_name))
context.register_custom_device(device, device_name, device_info)

self.assertTrue(context.is_custom_device(device_name))
self.assertFalse(context.is_custom_device('cpu:0'))
