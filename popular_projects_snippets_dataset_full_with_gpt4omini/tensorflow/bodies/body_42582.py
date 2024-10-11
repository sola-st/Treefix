# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
ctx = context.Context()

# Manually add a remote CPU device into logical device list.
ctx._logical_devices = []  # pylint: disable=protected-access
dev = context.LogicalDevice(name='/job:worker/replica:0/task:1',
                            device_type='CPU')
ctx._logical_devices.append(dev)  # pylint: disable=protected-access
self.assertIs(len(ctx.list_logical_devices('CPU')), 1)

# This would pass the check since the previously added device is not local.
ctx.set_logical_cpu_devices(4)
# Logical device list would be overwritten after initialization.
self.assertIs(len(ctx.list_logical_devices('CPU')), 4)
