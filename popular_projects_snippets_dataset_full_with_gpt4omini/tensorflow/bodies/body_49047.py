# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""This method captures TF's explicit device scope setting."""
if isinstance(device, device_spec.DeviceSpecV2):
    device = device.to_string()
self.device = device
