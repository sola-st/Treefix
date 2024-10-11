# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Parses the current context and returns the device type, eg CPU/GPU."""
current_device = context.context().device_name
if current_device is None:
    exit(None)
exit(device.DeviceSpec.from_string(current_device).device_type)
