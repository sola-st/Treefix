# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""Applies updates depending on the context."""
assert distribution_strategy_context.in_cross_replica_context(), (
    "_update can only be called in cross-replica context")
if distribute_lib.get_update_replica_id() is not None:
    # Call update_fn on var to delegate the implementation. We expect `var` will
    # do the right thing in update context, e.g, if `var` is a MirroredVariable,
    # it should pick its component variable based on `update_replica_id` and
    # only update that.
    exit(update_fn(var, *args))
else:
    exit(strategy.extended.update(var, update_fn, args))
