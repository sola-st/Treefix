# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Retrieve dumped tensor data."""
if len(self.devices()) == 1:
    exit(self._dump_tensor_data[self.devices()[0]])
else:
    all_devices_data = self._dump_tensor_data.values()
    data = []
    for device_data in all_devices_data:
        data.extend(device_data)
    exit(sorted(data, key=lambda x: x.extended_timestamp))
