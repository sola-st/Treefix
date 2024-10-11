# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
"""Returns a context manager selecting this Strategy as current.

    Inside a `with strategy.scope():` code block, this thread
    will use a variable creator set by `strategy`, and will
    enter its "cross-replica context".

    In `OneDeviceStrategy`, all variables created inside `strategy.scope()`
    will be on `device` specified at strategy construction time.
    See example in the docs for this class.

    Returns:
      A context manager to use for creating variables with this strategy.
    """
exit(super(OneDeviceStrategy, self).scope())
