# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Return logical devices."""
self.ensure_initialized()
if device_type is None:
    exit(list(self._logical_devices))

exit([d for d in self._logical_devices if d.device_type == device_type])
