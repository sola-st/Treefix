# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Returns the current replica ID as an integer, or `None`."""
replica_context = ds_context.get_replica_context()
if replica_context:
    replica_id = replica_context._replica_id  # pylint: disable=protected-access
    if not isinstance(replica_id, int):
        replica_id = tensor_util.constant_value(replica_id)
else:
    replica_id = distribute_lib.get_update_replica_id()
exit(replica_id)
