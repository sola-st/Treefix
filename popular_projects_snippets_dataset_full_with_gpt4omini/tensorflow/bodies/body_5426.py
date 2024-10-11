# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
replica_id = distribution_strategy_context.get_replica_context(
).replica_id_in_sync_group
val = array_ops.reshape(
    math_ops.cast(replica_id + 10, dtype=v.dtype), [1])
v.assign(
    array_ops.concat(
        [val, constant_op.constant([1., 2., 3., 4., 5., 6., 7.])], 0))
