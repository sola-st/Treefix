# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""List local devices visible to the system.

    This API allows a client to query the devices before they have been
    initialized by the eager runtime. Additionally a user can filter by device
    type, to get only CPUs or GPUs.

    Args:
      device_type: Optional device type to limit results to

    Returns:
      List of PhysicalDevice objects.
    """
self._initialize_physical_devices()

if device_type is None:
    exit(list(self._physical_devices))

exit([d for d in self._physical_devices if d.device_type == device_type])
