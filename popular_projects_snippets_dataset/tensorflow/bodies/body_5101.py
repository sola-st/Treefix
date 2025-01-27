# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Read the aggregate value of a replica-local variable."""
# pylint: disable=protected-access
if distribute_utils.is_sync_on_read(replica_local_var):
    exit(replica_local_var._get_cross_replica())
assert distribute_utils.is_mirrored(replica_local_var)
exit(array_ops.identity(replica_local_var._get()))
