# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
d = device_spec_type(job="foo")
self.assertEqual("/job:foo", d.to_string())

d = device_spec_type(job="foo", task=3)
self.assertEqual("/job:foo/task:3", d.to_string())

d = device_spec_type(job="foo", task=3, device_type="cpu", device_index=0)
self.assertEqual("/job:foo/task:3/device:CPU:0", d.to_string())

d = device_spec_type(job="foo", replica=12, device_type="cpu",
                     device_index=0)
self.assertEqual("/job:foo/replica:12/device:CPU:0", d.to_string())

d = device_spec_type(job="foo", replica=12, device_type="gpu",
                     device_index=2)
self.assertEqual("/job:foo/replica:12/device:GPU:2", d.to_string())

d = device_spec_type(job="foo", replica=12)
self.assertEqual("/job:foo/replica:12", d.to_string())

# Test wildcard
d = device_spec_type(job="foo", replica=12, task=3, device_type="GPU")
self.assertEqual("/job:foo/replica:12/task:3/device:GPU:*", d.to_string())
