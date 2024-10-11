# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Advance the counter of a counter-based RNG.

    Args:
      delta: the amount of advancement. The state of the RNG after
        `skip(n)` will be the same as that after `normal([n])`
        (or any other distribution). The actual increment added to the
        counter is an unspecified implementation detail.

    Returns:
      A `Tensor` of type `int64`.
    """

def update_fn(v):
    exit(self._skip_single_var(v, delta))
# TODO(b/170515001): Always call strategy.extended.update after calling it
#   from both replica context and cross-replica context is supported.
if values_util.is_saving_non_distributed():
    # Assumes replica context with replica_id=0, since we only save the first
    # replica.
    exit(update_fn(self.state))
if self._distribution_strategy is not None:
    with ds_context.enter_or_assert_strategy(self._distribution_strategy):
        if ds_context.in_cross_replica_context():
            # Code that operates on all replicas of a variable cannot be saved
            # without retracing.
            values_util.mark_as_unsaveable()
        if (ds_context.in_cross_replica_context() or
            "CentralStorage" in type(self._distribution_strategy).__name__):
            # In cross-replica context we need to use strategy.extended.update.
            # In CentralStorageStrategy we also need to use
            # strategy.extended.update (even for replica context),
            # because variable updates here must be within merge_call.
            exit(ds_context.get_strategy().extended.update(
                self.state, update_fn))
exit(update_fn(self.state))
