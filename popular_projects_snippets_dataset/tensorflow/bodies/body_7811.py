# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
value = array_ops.identity(1.0)
reduced = strategy.extended._replica_ctx_all_reduce(
    reduce_util.ReduceOp.SUM, value)
exit(reduced)
