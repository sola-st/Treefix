# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
with ops.Graph().as_default():
    with ops.device("/cpu:0"):
        self.assertEqual(device_util.current(), "/device:CPU:0")
