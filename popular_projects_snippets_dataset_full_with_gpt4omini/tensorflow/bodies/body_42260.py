# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Set the virtual device configuration for a PhysicalDevice."""
self._initialize_physical_devices()

if dev not in self._physical_devices:
    raise ValueError("Unrecognized device: %s" % repr(dev))

if dev.device_type == "CPU":
    for vdev in virtual_devices:
        if vdev.memory_limit is not None:
            raise ValueError("Setting memory limit on CPU virtual devices is "
                             "currently not supported")
        if vdev.experimental_priority is not None:
            raise ValueError("Setting experimental_priority on CPU virtual "
                             " devices is currently not supported")
        if vdev.experimental_device_ordinal is not None:
            raise ValueError("Setting experimental_device_ordinal on CPU virtual "
                             " devices is currently not supported")
elif dev.device_type == "GPU":
    for vdev in virtual_devices:
        if vdev.memory_limit is None:
            raise ValueError(
                "Setting memory limit is required for GPU virtual devices")
else:
    raise ValueError("Virtual devices are not supported for %s" %
                     dev.device_type)

if self._virtual_device_map.get(dev) == virtual_devices:
    exit()

if self._context_handle is not None:
    raise RuntimeError(
        "Virtual devices cannot be modified after being initialized")

self._virtual_device_map[dev] = virtual_devices
