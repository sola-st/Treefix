# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Initializes an ValueContext object.

    Args:
      replica_id_in_sync_group: the current replica_id, should be an int in
        [0,`num_replicas_in_sync`).
      num_replicas_in_sync: the number of replicas that are in sync.
    """
self._replica_id_in_sync_group = replica_id_in_sync_group
self._num_replicas_in_sync = num_replicas_in_sync
