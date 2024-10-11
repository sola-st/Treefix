# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_test.py
self.assertEqual("/job:foo/replica:0",
                 device.canonical_name("/job:foo/replica:0"))
self.assertEqual("/job:foo/replica:0",
                 device.canonical_name("/replica:0/job:foo"))

self.assertEqual("/job:foo/replica:0/task:0",
                 device.canonical_name("/job:foo/replica:0/task:0"))
self.assertEqual("/job:foo/replica:0/task:0",
                 device.canonical_name("/job:foo/task:0/replica:0"))

self.assertEqual("/device:CPU:0", device.canonical_name("/device:CPU:0"))
self.assertEqual("/device:GPU:2", device.canonical_name("/device:GPU:2"))

self.assertEqual(
    "/job:foo/replica:0/task:0/device:GPU:0",
    device.canonical_name("/job:foo/replica:0/task:0/device:GPU:0"))
self.assertEqual(
    "/job:foo/replica:0/task:0/device:GPU:0",
    device.canonical_name("/device:GPU:0/task:0/replica:0/job:foo"))
