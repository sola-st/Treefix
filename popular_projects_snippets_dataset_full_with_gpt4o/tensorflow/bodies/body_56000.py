# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
d = device_spec.DeviceSpecV1()
d.parse_from_string("/job:foo/replica:0")
self.assertEqual("/job:foo/replica:0", d.to_string())

d.parse_from_string("/replica:1/task:0/cpu:0")
self.assertEqual("/replica:1/task:0/device:CPU:0", d.to_string())

d.parse_from_string("/replica:1/task:0/device:CPU:0")
self.assertEqual("/replica:1/task:0/device:CPU:0", d.to_string())

d.parse_from_string("/job:muu/device:GPU:2")
self.assertEqual("/job:muu/device:GPU:2", d.to_string())

with self.assertRaisesRegex(ValueError,
                            "Multiple device types are not allowed"):
    d.parse_from_string("/job:muu/device:GPU:2/cpu:0")
