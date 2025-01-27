# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device.py
if isinstance(spec, device_spec.DeviceSpecV2):
    self._spec = spec
elif isinstance(spec, device_spec.DeviceSpecV1):
    # Capture a snapshot of spec.
    self._spec = spec.__class__.from_string(spec.to_string())
else:
    self._spec = DeviceSpec.from_string(spec)
