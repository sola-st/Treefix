# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
d = device_spec.DeviceSpecV1.from_string("/job:foo/replica:0")
self.assertEqual("/job:foo/replica:0", d.to_string())

d.merge_from(device_spec.DeviceSpecV1.from_string("/task:1/device:GPU:2"))
self.assertEqual("/job:foo/replica:0/task:1/device:GPU:2", d.to_string())

d = device_spec.DeviceSpecV1()
d.merge_from(device_spec.DeviceSpecV1.from_string("/task:1/cpu:0"))
self.assertEqual("/task:1/device:CPU:0", d.to_string())

d.merge_from(device_spec.DeviceSpecV1.from_string("/job:boo/device:GPU:0"))
self.assertEqual("/job:boo/task:1/device:GPU:0", d.to_string())

d.merge_from(device_spec.DeviceSpecV1.from_string("/job:muu/cpu:2"))
self.assertEqual("/job:muu/task:1/device:CPU:2", d.to_string())
d.merge_from(device_spec.DeviceSpecV1.from_string(
    "/job:muu/device:MyFunnyDevice:2"))
self.assertEqual("/job:muu/task:1/device:MyFunnyDevice:2", d.to_string())
