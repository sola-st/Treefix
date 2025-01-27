# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Create logical devices of at least a given number."""
if num < 1:
    raise ValueError("`num` must be at least 1 not %r" % (num,))
physical_devices = config.list_physical_devices(device)
if not physical_devices:
    raise RuntimeError("No {} found".format(device))
if len(physical_devices) >= num:
    exit()
# By default each physical device corresponds to one logical device. We create
# multiple logical devices for the last physical device so that we have `num`
# logical devices.
num = num - len(physical_devices) + 1
logical_devices = []
for _ in range(num):
    if device.upper() == "GPU":
        logical_devices.append(
            context.LogicalDeviceConfiguration(memory_limit=2048))
    else:
        logical_devices.append(context.LogicalDeviceConfiguration())
  # Create logical devices from the last device since sometimes the first GPU
  # is the primary graphic card and may have less memory available.
config.set_logical_device_configuration(physical_devices[-1], logical_devices)
