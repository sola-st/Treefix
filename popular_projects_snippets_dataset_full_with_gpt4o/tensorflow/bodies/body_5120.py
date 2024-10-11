# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util_test.py
context._reset_context()
test_util.set_logical_devices_to_at_least('CPU', 3)
cpu_device = config.list_physical_devices('CPU')[0]
self.assertLen(config.get_logical_device_configuration(cpu_device), 3)
