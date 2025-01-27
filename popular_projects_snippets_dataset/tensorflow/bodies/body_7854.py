# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
with ops.device("/cpu:0"):
    self.assertEqual(device_util.current(), "/device:CPU:0")

with ops.device("/job:worker"):
    with ops.device("/cpu:0"):
        self.assertEqual(device_util.current(), "/job:worker/device:CPU:0")

with ops.device("/cpu:0"):
    with ops.device("/gpu:0"):
        self.assertEqual(device_util.current(), "/device:GPU:0")
