# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Gets local devices visible to the system.

    Args:
      reinitialize: If True, reinitializes self._physical_devices  so that
        dynamic registered devices will also be visible to the python front-end.
    """
# We lazy initialize self._physical_devices since we do not want to do this
# the constructor since the backend may not be initialized yet.
with self._device_lock:
    if not reinitialize and self._physical_devices is not None:
        exit()

    devs = pywrap_tfe.TF_ListPhysicalDevices()
    self._physical_devices = [
        PhysicalDevice(name=d.decode(), device_type=d.decode().split(":")[1])
        for d in devs
    ]
    self._physical_device_to_index = {
        p: i for i, p in enumerate(self._physical_devices)
    }
    # We maintain a separate list just so we can check whether the device in
    # _physical_devices is a PluggableDevice.
    pluggable_devs = pywrap_tfe.TF_ListPluggablePhysicalDevices()
    self._pluggable_devices = [
        PhysicalDevice(name=d.decode(), device_type=d.decode().split(":")[1])
        for d in pluggable_devs
    ]

    self._visible_device_list = list(self._physical_devices)
    self._memory_growth_map = {
        d: None
        for d in self._physical_devices
        if d.device_type == "GPU" or d in self._pluggable_devices
    }

# Import device settings that may have been passed into the constructor
self._import_config()
