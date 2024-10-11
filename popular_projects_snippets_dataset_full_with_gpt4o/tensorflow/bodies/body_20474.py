# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
if isinstance(device, pydev.DeviceSpec):
    self._device = device.to_string()
else:
    self._device = device
