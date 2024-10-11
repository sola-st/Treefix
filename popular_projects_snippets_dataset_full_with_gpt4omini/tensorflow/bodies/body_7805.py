# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

exit(strategy.reduce(
    reduce_util.ReduceOp.SUM, value=per_replica_value, axis=None))
