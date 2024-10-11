# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Verify in `replica_ctx` replica context."""
context = _get_per_thread_mode()
if context.replica_context is replica_ctx: exit()
# We have an error to report, figure out the right message.
if context.replica_context is None:
    raise RuntimeError("Need to be inside `call_for_each_replica()`")
if context.strategy is replica_ctx.strategy:
    # Two different ReplicaContexts with the same tf.distribute.Strategy.
    raise RuntimeError("Mismatching ReplicaContext.")
raise RuntimeError(
    "Mismatching tf.distribute.Strategy objects: %s is not %s." %
    (context.strategy, replica_ctx.strategy))
