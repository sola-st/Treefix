# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
value_identity = array_ops.identity(value)
ctx = ds_context.get_replica_context()
exit(ctx.all_gather(value_identity, axis=1))
