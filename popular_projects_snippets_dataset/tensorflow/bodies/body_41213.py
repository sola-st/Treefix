# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
super().setUp()
cpus = config.list_physical_devices('CPU')
# Set 4 virtual CPUs
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])
