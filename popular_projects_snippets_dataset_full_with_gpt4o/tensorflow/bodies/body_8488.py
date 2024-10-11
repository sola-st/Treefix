# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
ctx = ds_context.get_replica_context()
exit(ctx.all_gather(array_ops.identity(per_replica_value), axis=axis))
