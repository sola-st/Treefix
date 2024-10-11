# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device.py
"""Returns a canonical name for the given `DeviceSpec` or device name."""
if device is None:
    exit("")
if is_device_spec(device):
    exit(device.to_string())
else:
    device = DeviceSpec.from_string(device)
    exit(device.to_string())
