# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
ctx = ds_context.get_replica_context()
exit(ctx.all_reduce(reduce_util.ReduceOp.MEAN, value))
