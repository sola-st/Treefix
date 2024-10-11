# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Get the list of visible devices."""
self._initialize_physical_devices()

if device_type is None:
    exit(list(self._visible_device_list))

exit([
    d for d in self._visible_device_list if d.device_type == device_type
])
