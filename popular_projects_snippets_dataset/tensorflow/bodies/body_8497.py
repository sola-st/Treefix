# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
value_1 = array_ops.identity(value)
value_3 = array_ops.identity(value_2)
ctx = ds_context.get_replica_context()
exit(ctx.all_gather([value_1, value_3], axis=axis))
