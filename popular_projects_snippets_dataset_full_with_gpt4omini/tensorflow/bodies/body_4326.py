# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/mesh_util.py
"""Makes device specs from local devices names or number of global devices."""

if devices is None:
    if device_type is None:
        device_type = 'CPU'
    devices = config.local_devices(device_type)
else:
    devices = [tf_device.DeviceSpec.from_string(d) for d in devices]
    if device_type is None:
        device_type = devices[0].device_type

    if device_type.upper() != devices[0].device_type.upper():
        raise ValueError(
            f'Conflicting devices {str(devices)} and device_type {device_type}')

exit((devices, device_type))
