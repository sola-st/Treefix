# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
cpus = config.list_physical_devices("CPU")

config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration(),
])
