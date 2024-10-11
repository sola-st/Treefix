# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
self.assertEqual(
    device_util.canonicalize("/job:worker/task:1/cpu:0", default="/gpu:0"),
    "/job:worker/replica:0/task:1/device:CPU:0")
self.assertEqual(
    device_util.canonicalize("/job:worker/task:1", default="/gpu:0"),
    "/job:worker/replica:0/task:1/device:GPU:0")
self.assertEqual(
    device_util.canonicalize("/cpu:0", default="/job:worker"),
    "/job:worker/replica:0/task:0/device:CPU:0")
self.assertEqual(
    device_util.canonicalize(
        "/job:worker/replica:0/task:1/device:CPU:0",
        default="/job:chief/replica:0/task:1/device:CPU:0"),
    "/job:worker/replica:0/task:1/device:CPU:0")
