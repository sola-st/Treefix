# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
super(SoftDevicePlacementTest, self).setUp()
context._reset_context()
context.ensure_initialized()
config.set_soft_device_placement(enabled=True)
context.context().log_device_placement = True
