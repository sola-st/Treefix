# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

def replica_fn():
    value1 = indexed_slices.IndexedSlices(
        values=array_ops.identity([[1.0]]),
        indices=array_ops.identity([0]),
        dense_shape=array_ops.identity([5, 1]))
    value2 = indexed_slices.IndexedSlices(
        values=array_ops.identity([[2.0]]),
        indices=array_ops.identity([0]),
        dense_shape=array_ops.identity([5, 1]))
    rep_ctx = ds_context.get_replica_context()
    reduced = rep_ctx.all_reduce(reduce_util.ReduceOp.SUM, [value1, value2])
    exit(reduced)

exit(strategy.experimental_local_results(strategy.run(replica_fn)))
