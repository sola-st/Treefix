# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Verify in cross-replica context."""
context = _get_per_thread_mode()
cross_replica = context.cross_replica_context
if cross_replica is not None and cross_replica.extended is extended:
    exit()
if context is _get_default_replica_mode():
    exit()
strategy = extended._container_strategy()  # pylint: disable=protected-access
# We have an error to report, figure out the right message.
if context.strategy is not strategy:
    _wrong_strategy_scope(strategy, context)
assert cross_replica is None
if not error_message:
    error_message = ("Method requires being in cross-replica context, use "
                     "get_replica_context().merge_call()")
raise RuntimeError(error_message)
