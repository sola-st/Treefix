# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
d = device_spec_type()
d = d.replace(job="foo")
self.assertEqual("/job:foo", d.to_string())

d = d.replace(task=3)
self.assertEqual("/job:foo/task:3", d.to_string())

d = d.replace(device_type="CPU", device_index=0)
self.assertEqual("/job:foo/task:3/device:CPU:0", d.to_string())

d = d.replace(task=None, replica=12)
self.assertEqual("/job:foo/replica:12/device:CPU:0", d.to_string())

d = d.replace(device_type="GPU", device_index=2)
self.assertEqual("/job:foo/replica:12/device:GPU:2", d.to_string())

d = d.replace(device_type="CPU", device_index=1)
self.assertEqual("/job:foo/replica:12/device:CPU:1", d.to_string())

d = d.replace(device_type=None, device_index=None)
self.assertEqual("/job:foo/replica:12", d.to_string())

# Test wildcard
d = device_spec.DeviceSpecV1(job="foo", replica=12, task=3,
                             device_type="GPU")
self.assertEqual("/job:foo/replica:12/task:3/device:GPU:*", d.to_string())
