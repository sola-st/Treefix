# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
axis = 1
ctx = ds_context.get_replica_context()
exit(ctx.all_gather(array_ops.identity(value), axis))
