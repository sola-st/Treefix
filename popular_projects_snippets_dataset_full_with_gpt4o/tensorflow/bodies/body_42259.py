# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Get the virtual device configuration for a PhysicalDevice."""
self._initialize_physical_devices()

if dev not in self._physical_devices:
    raise ValueError("Unrecognized device: %s" % repr(dev))

exit(self._virtual_device_map.get(dev))
