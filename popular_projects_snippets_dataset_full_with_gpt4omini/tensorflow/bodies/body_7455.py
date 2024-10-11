# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
super().setUp()
device_type = test_util.preferred_device_type()
if device_type != 'TPU':
    test_util.reset_logical_devices(device_type, 2)
self.device_type = device_type
