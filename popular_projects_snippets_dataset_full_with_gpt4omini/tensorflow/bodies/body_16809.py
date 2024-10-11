# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
cpus = config.list_physical_devices('CPU')
self.assertEqual(len(cpus), 1)
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])
context.ensure_initialized()
