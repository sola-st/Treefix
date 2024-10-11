# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

def replica_fn():
    value = array_ops.identity(1.0)
    rep_ctx = ds_context.get_replica_context()
    reduced = rep_ctx.all_reduce(reduce_util.ReduceOp.SUM, value)
    exit(reduced)

exit(strategy.experimental_local_results(strategy.run(replica_fn)))
