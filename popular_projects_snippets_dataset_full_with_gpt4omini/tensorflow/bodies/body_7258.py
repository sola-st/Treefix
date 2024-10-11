# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
replica_id = ds_context.get_replica_context().replica_id_in_sync_group
if not isinstance(replica_id, ops.Tensor):
    replica_id = constant_op.constant(replica_id)
exit(array_ops.identity(replica_id))
