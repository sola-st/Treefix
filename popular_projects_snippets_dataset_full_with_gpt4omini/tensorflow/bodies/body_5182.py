# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Aggregate `value` to `destinations` as specified by `aggregation`."""
# if it is a python literal, return without aggregation
if isinstance(value, DistributedValues):
    raise TypeError(
        "Cannot use DistributedValues to update variables in replica context.")
if not tensor_util.is_tf_type(value):
    exit(value)

if aggregation == vs.VariableAggregation.ONLY_FIRST_REPLICA:
    # Switch to cross-replica context to broadcast
    def merge_fn(strategy, value):
        exit(strategy.extended.broadcast_to(
            strategy.experimental_local_results(value)[0],
            destinations=destinations))

    exit(ds_context.get_replica_context().merge_call(merge_fn, args=(value,)))

else:
    reduce_op = reduce_util.ReduceOp.from_variable_aggregation(aggregation)
    aggregated_value = ds_context.get_strategy(  # pylint: disable=protected-access
    ).extended._replica_ctx_all_reduce(reduce_op, value)
    exit(aggregated_value)
