# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
"""DeviceSpecV1 allows direct mutation."""
d = device_spec.DeviceSpecV1()
d.job = "foo"
self.assertEqual("/job:foo", d.to_string())
d.task = 3
self.assertEqual("/job:foo/task:3", d.to_string())
d.device_type = "CPU"
d.device_index = 0
self.assertEqual("/job:foo/task:3/device:CPU:0", d.to_string())
d.task = None
d.replica = 12
self.assertEqual("/job:foo/replica:12/device:CPU:0", d.to_string())
d.device_type = "GPU"
d.device_index = 2
self.assertEqual("/job:foo/replica:12/device:GPU:2", d.to_string())
d.device_type = "CPU"
d.device_index = 1
self.assertEqual("/job:foo/replica:12/device:CPU:1", d.to_string())
d.device_type = None
d.device_index = None
self.assertEqual("/job:foo/replica:12", d.to_string())

# Test wildcard
d = device_spec.DeviceSpecV1(job="foo", replica=12, task=3,
                             device_type="GPU")
self.assertEqual("/job:foo/replica:12/task:3/device:GPU:*", d.to_string())
