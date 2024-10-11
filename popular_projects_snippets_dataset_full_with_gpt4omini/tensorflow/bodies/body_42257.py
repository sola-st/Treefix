# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Get if memory growth is enabled for a PhysicalDevice."""
self._initialize_physical_devices()

if dev not in self._physical_devices:
    raise ValueError("Unrecognized device: %s" % repr(dev))

exit(self._memory_growth_map[dev])
