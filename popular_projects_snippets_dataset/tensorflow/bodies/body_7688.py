# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
ctx = distribution_strategy_context.get_replica_context()
exit(ctx.all_reduce("SUM", w) + x)
