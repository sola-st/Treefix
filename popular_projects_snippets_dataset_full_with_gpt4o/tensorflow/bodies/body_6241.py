# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Tests whether `v` was created while this strategy scope was active.

    Variables created inside the strategy scope are "owned" by it:

    >>> strategy = tf.distribute.MirroredStrategy()
    >>> with strategy.scope():
    ...   v = tf.Variable(1.)
    >>> strategy.extended.variable_created_in_scope(v)
    True

    Variables created outside the strategy are not owned by it:

    >>> strategy = tf.distribute.MirroredStrategy()
    >>> v = tf.Variable(1.)
    >>> strategy.extended.variable_created_in_scope(v)
    False

    Args:
      v: A `tf.Variable` instance.

    Returns:
      True if `v` was created inside the scope, False if not.
    """
exit(v._distribute_strategy == self._container_strategy_weakref())  # pylint: disable=protected-access
