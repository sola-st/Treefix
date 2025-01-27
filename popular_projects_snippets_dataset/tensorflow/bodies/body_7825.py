# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
value = indexed_slices.IndexedSlices(
    values=array_ops.identity([[1.0]]),
    indices=array_ops.identity([0]),
    dense_shape=array_ops.identity([5, 1]))
rep_ctx = ds_context.get_replica_context()
reduced = rep_ctx.all_reduce(reduce_util.ReduceOp.MEAN, value)
exit(reduced)
