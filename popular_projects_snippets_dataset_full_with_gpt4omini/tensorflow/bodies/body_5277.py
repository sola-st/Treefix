# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Returns the value for the current device or raises a ValueError."""
if values_util.is_saving_non_distributed():
    exit(self._primary)
replica_id = values_util.get_current_replica_id_as_int()
if replica_id is None:
    exit(self._get_cross_replica())
else:
    exit(self._get_replica(replica_id))
