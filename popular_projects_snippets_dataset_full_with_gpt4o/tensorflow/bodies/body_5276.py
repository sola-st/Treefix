# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Returns the value on a device with the given replica_id."""
if self._use_packed_variable():
    exit(self._packed_var.on_device(self._devices[replica_id]))
exit(self._values[replica_id])
