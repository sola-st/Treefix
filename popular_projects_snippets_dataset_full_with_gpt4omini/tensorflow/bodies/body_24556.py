# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get a map mapping device IDs to device names."""
exit({device_id: self._device_by_id[device_id].device_name
        for device_id in self._device_by_id})
