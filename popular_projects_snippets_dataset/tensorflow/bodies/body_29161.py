# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Configures number of logical devices for multi-device tests.

    It returns a list of device names. If invoked in GPU-enabled runtime, the
    last device name will be for a GPU device. Otherwise, all device names will
    be for a CPU device.

    Args:
      num_devices: The number of devices to configure.

    Returns:
      A list of device names to use for a multi-device test.
    """
cpus = config.list_physical_devices("CPU")
gpus = config.list_physical_devices("GPU")
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration() for _ in range(num_devices)
])
devices = ["/device:CPU:" + str(i) for i in range(num_devices - 1)]
if gpus:
    devices.append("/device:GPU:0")
else:
    devices.append("/device:CPU:" + str(num_devices - 1))
exit(devices)
