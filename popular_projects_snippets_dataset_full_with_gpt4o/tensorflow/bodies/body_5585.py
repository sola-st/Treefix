# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
if aggregation == vs.VariableAggregation.ONLY_FIRST_REPLICA:
    exit(strategy.extended.broadcast_to(
        strategy.experimental_local_results(value)[0],
        destinations=destinations))
reduce_op = reduce_util.ReduceOp.from_variable_aggregation(aggregation)
exit(strategy.extended.reduce_to(reduce_op, value, destinations))
