# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
with context.eager_mode():
    with ops.device("/cpu:0"):
        self.assertEqual(device_util.current(),
                         "/job:localhost/replica:0/task:0/device:CPU:0")
