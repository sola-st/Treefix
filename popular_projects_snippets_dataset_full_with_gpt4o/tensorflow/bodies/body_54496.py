# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
super(PackEagerTensorTest, self).setUp()
context._reset_context()
cpus = config.list_physical_devices("CPU")
# Set 2 virtual CPUs
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration(),
])
