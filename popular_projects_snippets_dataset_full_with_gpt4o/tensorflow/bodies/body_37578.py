# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
context._reset_context()
test_util.set_logical_devices_to_at_least('CPU', num_devices)
context.ensure_initialized()
context.set_log_device_placement(True)
