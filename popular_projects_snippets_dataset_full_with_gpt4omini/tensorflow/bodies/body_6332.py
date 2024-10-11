# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
with ReplicaContext(self._container_strategy(), replica_id_in_sync_group=0):
    exit(fn(*args, **kwargs))
