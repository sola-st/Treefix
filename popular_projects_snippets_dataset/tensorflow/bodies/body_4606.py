# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
super(PackedDistributedVariableTest, self).setUp()
cpus = config.list_physical_devices('CPU')
# Set 2 virtual CPUs
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration(),
])
