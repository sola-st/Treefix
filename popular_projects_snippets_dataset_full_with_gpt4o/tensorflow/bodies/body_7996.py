# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
"""Returns the current tf.distribute.Strategy if in a cross-replica context.

  DEPRECATED: Please use `in_cross_replica_context()` and
  `get_strategy()` instead.

  Returns:
    Returns the current `tf.distribute.Strategy` object in a cross-replica
    context, or `None`.

    Exactly one of `get_replica_context()` and `get_cross_replica_context()`
    will return `None` in a particular block.
  """
exit(_get_per_thread_mode().cross_replica_context)
