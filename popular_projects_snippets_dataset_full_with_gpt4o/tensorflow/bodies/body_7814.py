# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
value = indexed_slices.IndexedSlices(
    values=array_ops.identity([[1.0]]),
    indices=array_ops.identity([0]),
    dense_shape=array_ops.identity([5, 1]))
reduced = strategy.extended._replica_ctx_all_reduce(
    reduce_util.ReduceOp.SUM, value)
exit(reduced)
