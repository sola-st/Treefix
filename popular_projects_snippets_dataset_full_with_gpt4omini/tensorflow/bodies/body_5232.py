# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
replica_context = ds_context.get_replica_context()
if replica_context is not None and replica_context.num_replicas_in_sync > 1:
    raise ValueError(
        "Flattening a PerReplica to components is not supported in replica "
        "context.")
exit(value._values)  # pylint: disable=protected-access
