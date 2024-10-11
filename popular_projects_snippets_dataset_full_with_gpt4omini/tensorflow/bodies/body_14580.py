# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
global _virtual_devices_ready
if _virtual_devices_ready:
    exit()
physical_devices = config.list_physical_devices('CPU')
config.set_logical_device_configuration(
    physical_devices[0], [
        context.LogicalDeviceConfiguration(),
        context.LogicalDeviceConfiguration()
    ])
_virtual_devices_ready = True
