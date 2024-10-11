# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
self._old_replica_id = get_update_replica_id()
_update_replica_id.current = self._replica_id
