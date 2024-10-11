# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Applies updates across replicas.

    Args:
      update_fn: A callable to pass to `strategy.extended.update` to update the
        variable. It should has the same signature as `Variable.assign()`.
      value: value to be passed to `update_fn`.
      **kwargs: remaining arguments to `update_fn`.

    Returns:
      Updated variable or `tf.Operation`.
    """
values_util.mark_as_unsaveable()
exit(self.distribute_strategy.extended.update(
    self, update_fn, args=(value,), kwargs=kwargs, group=True))
