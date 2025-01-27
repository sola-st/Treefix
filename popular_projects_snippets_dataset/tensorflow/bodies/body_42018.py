# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
super(HardDevicePlacementTest, self).setUp()
context._reset_context()
config.set_soft_device_placement(enabled=False)
context.context().log_device_placement = True
cpus = context.context().list_physical_devices('CPU')
# Set 2 virtual CPUs
context.context().set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])
self.assertEqual(config.get_soft_device_placement(), False)
self.assertEqual(context.context().soft_device_placement, False)
