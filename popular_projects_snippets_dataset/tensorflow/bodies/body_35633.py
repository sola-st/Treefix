# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
super(StatefulRandomOpsTest, self).setUp()
physical_devices = config.list_physical_devices("CPU")
config.set_logical_device_configuration(
    physical_devices[0], [
        context.LogicalDeviceConfiguration(),
        context.LogicalDeviceConfiguration()
    ])
