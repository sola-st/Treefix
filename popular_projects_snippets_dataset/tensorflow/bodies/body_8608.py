# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with self.device:
    exit(self.device.unpack(array_ops.ones([])))
