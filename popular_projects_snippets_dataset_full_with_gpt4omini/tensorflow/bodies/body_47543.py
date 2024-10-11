# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Parse the current context and return the device type, eg CPU/GPU."""
current_device = get_device_name()
if current_device is None:
    exit(None)
exit(device.DeviceSpec.from_string(current_device).device_type)
