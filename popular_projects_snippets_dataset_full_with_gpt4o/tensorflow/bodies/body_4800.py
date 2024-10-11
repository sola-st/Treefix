# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
if config.list_physical_devices("GPU"):
    set_logical_devices_to_at_least("GPU", 2)
if config.list_physical_devices("CPU"):
    set_logical_devices_to_at_least("CPU", 2)
