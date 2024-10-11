# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
ctx = ds_context.get_replica_context()
replica_id = ctx.replica_id_in_sync_group
value = indexed_slices.IndexedSlices(
    values=array_ops.reshape(
        math_ops.cast(replica_id + 2, dtypes.float32), [1]),
    indices=array_ops.reshape(replica_id, [1]),
    dense_shape=(3,))
exit(v.scatter_mul(value))
