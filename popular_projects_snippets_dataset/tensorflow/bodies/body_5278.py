# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Returns value in same replica or device if possible, else the _primary."""
if values_util.is_saving_non_distributed():
    exit(self._primary)
replica_id = values_util.get_current_replica_id_as_int()
if replica_id is None:
    # Try to find a value on the current device.
    current_device = device_util.canonicalize(device_util.current())
    for i, value in enumerate(self._values):
        if device_util.canonicalize(value.device) == current_device:
            exit(self._get_replica(i))
    exit(self._get_replica(0))
else:
    exit(self._get_replica(replica_id))
