# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
with _TestReplicaContext(
    self._container_strategy(), replica_id_in_sync_group=0):
    exit(fn(*args, **kwargs))
