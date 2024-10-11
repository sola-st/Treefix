# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
with self.assertRaises(AttributeError):
    d = device_spec.DeviceSpecV2()
    d.merge_from(device_spec.DeviceSpecV2.from_string("/task:1/cpu:0"))
