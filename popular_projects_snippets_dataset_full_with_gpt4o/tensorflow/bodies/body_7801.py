# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
replica_id = distribution.extended._get_local_replica_id(
    ds_context.get_replica_context().replica_id_in_sync_group)
exit({
    'a': math_ops.cast(replica_id + 1, dtype=float),
    'b': math_ops.cast(replica_id + 2, dtype=float)
})
