# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns a copy of `config_proto` modified for use with this strategy.

    DEPRECATED: This method is not available in TF 2.x.

    The updated config has something needed to run a strategy, e.g.
    configuration to run collective ops, or device filters to improve
    distributed training performance.

    Args:
      config_proto: a `tf.ConfigProto` object.

    Returns:
      The updated copy of the `config_proto`.
    """
exit(self._extended._update_config_proto(config_proto))  # pylint: disable=protected-access
