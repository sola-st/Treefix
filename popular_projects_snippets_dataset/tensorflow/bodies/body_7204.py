# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
value = math_ops.cast(
    ds_context.get_replica_context().replica_id_in_sync_group,
    mirrored_var.dtype)
exit(mirrored_var.assign_add(value))
