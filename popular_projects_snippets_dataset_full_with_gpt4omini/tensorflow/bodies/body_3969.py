# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Resets logical devices for CPU/GPU.

  Logical devices can only be instantiated once on a particular context. For
  now, context re-use is triggering some function duplication errors, so we
  reset the context on each call.

  Args:
    device_type: The device_type to reset.
    count: numbers of virtual device to reset to.
  """
reset_context()
devices = tf_config.list_physical_devices(device_type)
if device_type.upper() not in ('CPU', 'GPU'):
    raise ValueError('resetting logical device for non-supported device type : '
                     '%s' % device_type)

if count < len(devices):
    raise ValueError(f'Cannot set {count} logical devices, which is '
                     f'less than ({len(devices)}) physical devices.')

for i, device in enumerate(devices):
    n = (i + 1) * count // len(devices) - i * count // len(devices)
    assert n > 0  # guaranteed if count >= len(devices)
    configs = []
    for ordinal in range(n):
        if device_type.upper() == 'GPU':
            dev_config = context.LogicalDeviceConfiguration(
                memory_limit=_DEFAULT_GPU_MEMORY_LIMIT,
                experimental_device_ordinal=ordinal)
        else:
            dev_config = context.LogicalDeviceConfiguration()
        configs.append(dev_config)

    tf_config.set_logical_device_configuration(device, configs)
