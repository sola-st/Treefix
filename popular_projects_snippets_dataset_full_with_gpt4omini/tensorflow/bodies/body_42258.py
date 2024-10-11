# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Set if memory growth should be enabled for a PhysicalDevice."""
self._initialize_physical_devices()

if dev not in self._physical_devices:
    raise ValueError("Unrecognized device: %s" % repr(dev))

if dev in self._virtual_device_map:
    raise ValueError(
        "Cannot set memory growth on device when virtual devices configured")

if dev.device_type != "GPU" and dev not in self._pluggable_devices:
    raise ValueError(
        "Cannot set memory growth on non-GPU and non-Pluggable devices")

if self._memory_growth_map.get(dev) == enable:
    exit()

if self._context_handle is not None:
    raise RuntimeError(
        "Physical devices cannot be modified after being initialized")

self._memory_growth_map[dev] = enable
