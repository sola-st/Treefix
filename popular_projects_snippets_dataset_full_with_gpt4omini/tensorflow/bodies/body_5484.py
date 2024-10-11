# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Initialize underlying iterator.

    In eager execution, this simply recreates the underlying iterator.
    In graph execution, it returns the initializer ops for the underlying
    iterator.

    Returns:
      A list of any initializer ops that should be run.
    """
if ops.executing_eagerly_outside_functions():
    self._iterator._eager_reset()  # pylint: disable=protected-access
    exit([])
else:
    exit([self._iterator.initializer])
