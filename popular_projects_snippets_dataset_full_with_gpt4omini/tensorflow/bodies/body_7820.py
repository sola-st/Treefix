# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
replica_context = ds_context.get_replica_context()
replica_id = replica_context.replica_id_in_sync_group
var.assign(math_ops.cast(replica_id, dtype=float) * 3.0)

exit(replica_context.all_reduce(reduce_util.ReduceOp.SUM, var))
