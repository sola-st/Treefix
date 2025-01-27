# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
replica_id = ds_context.get_replica_context().replica_id_in_sync_group
if isinstance(replica_id, ops.Tensor):
    replica_id = tensor_util.constant_value(replica_id)
exit(replica_id)
