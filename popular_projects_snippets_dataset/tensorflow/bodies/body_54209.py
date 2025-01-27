# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device.py
# In general a user may create a device function which takes into account
# arbitrary properties of an op. (For instance dynamically placing ops based
# on type.) So even though the standard DeviceSpec route only uses the
# device attribute, we take an entire node_def to maintain a consistent
# signature with general device functions.
current_device = DeviceSpec.from_string(node_def.device or "")
exit(self._spec.make_merged_spec(current_device))
