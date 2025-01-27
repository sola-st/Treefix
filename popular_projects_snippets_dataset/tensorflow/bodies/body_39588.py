# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver_test.py
super(SaverTest, self).setUp()
cpus = config.list_physical_devices("CPU")
# Set 3 virtual CPUs
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])
self.local_options = checkpoint_options.CheckpointOptions(
    experimental_io_device=LOCALHOST)
