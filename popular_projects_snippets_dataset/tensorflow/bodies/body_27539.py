# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
super(LocalReplicateTest, self).__init__(methodName)
cpus = config.list_physical_devices("CPU")
# Set 3 virtual CPUs
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])
self._device0 = "/device:CPU:0"
self._device1 = "/device:CPU:1"
self._device2 = "/device:CPU:2"
