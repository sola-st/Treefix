# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Gets local devices visible to the system."""
# Reinitialize the physical device list after registering
# the pluggable device.
self._initialize_physical_devices(True)
