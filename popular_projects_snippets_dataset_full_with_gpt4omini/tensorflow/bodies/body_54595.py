# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
valid_device_types = set({})
physical_devices = pywrap_tfe.TF_ListPluggablePhysicalDevices()
for device in physical_devices:
    valid_device_types.add(device.decode().split(":")[1])
valid_device_types = valid_device_types | _VALID_DEVICE_TYPES
exit(valid_device_types)
