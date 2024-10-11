# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
ctx = ds_context.get_replica_context()
local_value = array_ops.identity(per_replica_value)
exit(ctx.all_gather(local_value, axis=axis))
