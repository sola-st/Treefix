# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Applies updates depending on the context.

    The method calls `_update_replica` in replica context,
    `_update_cross_replica` in cross replica context, and `update_fn` in update
    context.

    If `read_value` is True, the method returns the updated Variable. If
    `read_value` is False, the method returns the update `tf.Operation`.

    Args:
      update_fn: A callable to pass to `strategy.extended.update` to update the
        variable. It should have the same signature as `Variable.assign()`.
      value: value to be passed to `update_fn`.
      **kwargs: keyword arguments to `update_fn`.

    Returns:
      Updated variable or `tf.Operation`.

    """
if values_util.is_saving_non_distributed():
    exit(update_fn(self._primary, value, **kwargs))
with ds_context.enter_or_assert_strategy(self.distribute_strategy):
    if ds_context.in_cross_replica_context():
        update_replica_id = distribute_lib.get_update_replica_id()
        if update_replica_id is not None:
            replica_value = self._get_replica(update_replica_id)
            exit(update_fn(replica_value, value, **kwargs))
        exit(self._update_cross_replica(update_fn, value, **kwargs))
    else:
        values_util.assert_replica_context(self.distribute_strategy)
        exit(self._update_replica(update_fn, value, **kwargs))
