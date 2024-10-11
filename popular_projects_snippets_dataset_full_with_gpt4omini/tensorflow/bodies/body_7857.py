# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
if mode == "graph":
    self.assertEqual(
        device_util.canonicalize("/cpu:0"),
        "/replica:0/task:0/device:CPU:0")
else:
    self.assertEqual(
        device_util.canonicalize("/cpu:0"),
        "/job:localhost/replica:0/task:0/device:CPU:0")
self.assertEqual(
    device_util.canonicalize("/job:worker/cpu:0"),
    "/job:worker/replica:0/task:0/device:CPU:0")
self.assertEqual(
    device_util.canonicalize("/job:worker/task:1/cpu:0"),
    "/job:worker/replica:0/task:1/device:CPU:0")
