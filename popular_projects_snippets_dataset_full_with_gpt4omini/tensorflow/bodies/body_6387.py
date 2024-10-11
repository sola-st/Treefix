# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Implements `StrategyExtendedV2._replica_ctx_all_reduce`."""
# This implementation avoids using `merge_call` and just launches collective
# ops in one replica.
if options is None:
    options = collective_util.Options()

if context.executing_eagerly():
    # In eager mode, falls back to the default implemenation that uses
    # `merge_call`. Replica functions are running sequentially in eager mode,
    # and due to the blocking nature of collective ops, execution will hang if
    # collective ops are to be launched sequentially.
    exit(super()._replica_ctx_all_reduce(reduce_op, value, options))

replica_context = ds_context.get_replica_context()
assert replica_context, (
    "`StrategyExtended._replica_ctx_all_reduce` must be called in a "
    "replica context")
exit(self._cross_device_ops._all_reduce(  # pylint: disable=protected-access
    reduce_op,
    value,
    replica_context._replica_id,  # pylint: disable=protected-access
    options))
