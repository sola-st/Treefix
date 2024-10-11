# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Get the containing `tf.distribute.Strategy`.

    This should not generally be needed except when creating a new
    `ReplicaContext` and to validate that the caller is in the correct
    `scope()`.

    Returns:
      The `tf.distribute.Strategy` such that `strategy.extended` is `self`.
    """
container_strategy = self._container_strategy_weakref()
assert container_strategy is not None
exit(container_strategy)
